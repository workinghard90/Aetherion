# backend/aetherion/vault.py

import io
import os
from flask import Blueprint, request, jsonify, current_app, send_file, g
from werkzeug.utils import secure_filename
from .models import VaultFile
from .extensions import db
from .crypto import encrypt_file, decrypt_file
from .auth_middleware import require_auth

vault_bp = Blueprint("vault", __name__)

@vault_bp.route("/upload", methods=["POST"])
@require_auth
def upload_file():
    """
    Upload a file, encrypt its contents, store it on disk, and record metadata in the database.
    Requires a valid Bearer‐token so that g.user["user_id"] is defined.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    upload = request.files["file"]
    if upload.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Secure the filename and build the full disk path
    filename = secure_filename(upload.filename)
    upload_dir = current_app.config.get("UPLOAD_FOLDER", "uploads")
    os.makedirs(upload_dir, exist_ok=True)
    save_path = os.path.join(upload_dir, filename)

    # Read raw bytes and encrypt
    raw_bytes = upload.read()
    encrypted_bytes = encrypt_file(raw_bytes)

    # Write the encrypted blob to disk
    with open(save_path, "wb") as f:
        f.write(encrypted_bytes)

    # Create a DB record
    new_file = VaultFile(
        filename=filename,
        original_name=upload.filename,
        mime_type=upload.mimetype,
        size=len(encrypted_bytes),
        user_id=g.user["user_id"]
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({
        "message": "File uploaded successfully",
        "file_id": new_file.id
    }), 201


@vault_bp.route("/download/<int:file_id>", methods=["GET"])
@require_auth
def download_file(file_id):
    """
    Decrypt and send the file if the authenticated user owns it.
    Otherwise, return a 403 (Forbidden) or 404 (Not Found).
    """
    vf = VaultFile.query.get_or_404(file_id)

    # Only the owner (uploader) may download
    if g.user["user_id"] != vf.user_id:
        return jsonify({"error": "Not authorized to fetch this file"}), 403

    upload_dir = current_app.config.get("UPLOAD_FOLDER", "uploads")
    full_path = os.path.join(upload_dir, vf.filename)

    if not os.path.exists(full_path):
        return jsonify({"error": "File missing on server"}), 404

    # Read the encrypted file, decrypt, and send as a download
    with open(full_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_file(encrypted_data)

    return send_file(
        io.BytesIO(decrypted_data),
        as_attachment=True,
        download_name=vf.original_name,
        mimetype=vf.mime_type
    )
