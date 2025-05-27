# services/backend/app/api/vault.py

import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from ..models.file import VaultFile
from ..database import db
from ..services.crypto import encrypt_file, decrypt_file
from ..services.auth import require_auth

vault_bp = Blueprint("vault", __name__)

@vault_bp.route("/upload", methods=["POST"])
@require_auth
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)

    encrypted_data = encrypt_file(file.read())
    with open(path, "wb") as f:
        f.write(encrypted_data)

    new_file = VaultFile(
        filename=filename,
        original_name=file.filename,
        mime_type=file.mimetype,
        size=len(encrypted_data),
        user_id=request.user_id
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "file_id": new_file.id}), 201

@vault_bp.route("/files", methods=["GET"])
@require_auth
def list_files():
    files = VaultFile.query.filter_by(user_id=request.user_id).all()
    return jsonify([
        {
            "id": f.id,
            "name": f.original_name,
            "type": f.mime_type,
            "size": f.size,
            "uploaded": f.upload_time.isoformat()
        } for f in files
    ])

@vault_bp.route("/download/<int:file_id>", methods=["GET"])
@require_auth
def download_file(file_id):
    vault_file = VaultFile.query.filter_by(id=file_id, user_id=request.user_id).first()
    if not vault_file:
        return jsonify({"error": "File not found"}), 404

    path = os.path.join(current_app.config["UPLOAD_FOLDER"], vault_file.filename)
    if not os.path.exists(path):
        return jsonify({"error": "Encrypted file missing"}), 404

    with open(path, "rb") as f:
        decrypted_data = decrypt_file(f.read())

    return (
        decrypted_data,
        200,
        {
            "Content-Type": vault_file.mime_type,
            "Content-Disposition": f"attachment; filename={vault_file.original_name}"
        },
    )

@vault_bp.route("/delete/<int:file_id>", methods=["DELETE"])
@require_auth
def delete_file(file_id):
    vault_file = VaultFile.query.filter_by(id=file_id, user_id=request.user_id).first()
    if not vault_file:
        return jsonify({"error": "File not found"}), 404

    path = os.path.join(current_app.config["UPLOAD_FOLDER"], vault_file.filename)
    if os.path.exists(path):
        os.remove(path)

    db.session.delete(vault_file)
    db.session.commit()

    return jsonify({"message": "File deleted"}), 200
