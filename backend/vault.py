import os
from flask import Blueprint, request, jsonify, current_app, send_file
from werkzeug.utils import secure_filename
from extensions import db
from models import VaultFile
from crypto import encrypt_file, decrypt_file
from auth import require_auth

vault_bp = Blueprint("vault", __name__)

@vault_bp.route("/vault/upload", methods=["POST"])
@require_auth
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)
    path = os.path.join(upload_folder, filename)

    encrypted_data = encrypt_file(file.read())
    with open(path, "wb") as f:
        f.write(encrypted_data)

    new_file = VaultFile(
        filename=filename,
        original_name=file.filename,
        mime_type=file.mimetype,
        size=len(encrypted_data),
        user_id=request.g.user.id
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "file_id": new_file.id}), 201

@vault_bp.route("/vault/download/<int:file_id>", methods=["GET"])
@require_auth
def download_file(file_id):
    vf = VaultFile.query.get_or_404(file_id)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    path = os.path.join(upload_folder, vf.filename)
    if not os.path.exists(path):
        return jsonify({"error": "File not found on server"}), 404

    with open(path, "rb") as f:
        decrypted = decrypt_file(f.read())

    # Temporarily write to a local file to send, or use BytesIO
    from io import BytesIO
    bio = BytesIO(decrypted)
    bio.seek(0)
    return send_file(
        bio,
        download_name=vf.original_name,
        mimetype=vf.mime_type,
        as_attachment=True
    )
