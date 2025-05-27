# services/backend/app/api/vault.py

import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from ..models.file import VaultFile
from ..database import db

vault_bp = Blueprint("vault", __name__)

@vault_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
    file.save(path)

    new_file = VaultFile(
        filename=filename,
        original_name=file.filename,
        mime_type=file.mimetype,
        size=os.path.getsize(path),
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "file_id": new_file.id}), 201

@vault_bp.route("/files", methods=["GET"])
def list_files():
    files = VaultFile.query.all()
    return jsonify([
        {
            "id": f.id,
            "name": f.original_name,
            "type": f.mime_type,
            "size": f.size,
            "uploaded": f.upload_time.isoformat()
        } for f in files
    ])
