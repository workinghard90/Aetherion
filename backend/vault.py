# backend/vault.py

import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from .extensions import db
from .core.crypto import encrypt_file, decrypt_file   # Adjust paths if needed
from .core.auth import require_auth                     # Adjust paths if needed
from .models.file import VaultFile                      # Adjust paths if needed

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
        user_id=request.user_id
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "file_id": new_file.id}), 201

