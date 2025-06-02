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
    Upload a file, encrypt it, save to disk, store metadata.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    upload_dir = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_dir, exist_ok=True)
    save_path = os.path.join(upload_dir, filename)

    encrypted_data = encrypt_file(file.read())
    with open(save_path, "wb") as f:
        f.write(encrypted_data)

    new_file = VaultFile(
        filename=filename,
        original_name=file.filename,
        mime_type=file.mimetype,
        size=len(encrypted_data),
        user_id=g.user["user_id"]
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "file_id": new_file.id}), 201

@vault_bp.route("/download/<int:file_id>", methods=["GET"])
@require_auth
def download_file(file_id):
    """
    If the authenticated user uploaded this file, decrypt and send it.
    Otherwise, 404 or forbidden.
    """
    vf = VaultFile.query.get_or_404(file_id)
    if g.user["user_id"] != vf.user_id:
        return jsonify({"error": "Not authorized to fetch this file"}), 403

    upload_dir = current_app.config["UPLOAD_FOLDER"]
    full_path = os.path.join(upload_dir, vf.filename)
    if not os.path.exists(full_path):
        return jsonify({"error": "File missing on server"}), 404

    with open(full_path, "rb") as f:
        decrypted = decrypt_file(f.read())

    return send_file(
        io.BytesIO(decrypted),
        download_name=vf.original_name,
        mimetype=vf.mime_type
    )
