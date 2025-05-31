from flask import Blueprint, request, jsonify, current_app, g
from werkzeug.utils import secure_filename
import os
from .models.file import VaultFile
from .extensions import db
from .crypto import encrypt_file, decrypt_file
from .auth import require_auth

vault_bp = Blueprint("vault", __name__, url_prefix="/api/vault")

@vault_bp.before_request
def attach_optional_user():
    # Either use require_auth on each route or do silent auth
    # Or do nothing here if all vault routes require auth
    pass

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
    file_path = os.path.join(upload_folder, filename)

    encrypted_data = encrypt_file(file.read())
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

    new_file = VaultFile(
        filename=filename,
        original_name=file.filename,
        mime_type=file.mimetype,
        size=len(encrypted_data),
        user_id=g.user_id
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "file_id": new_file.id}), 201

@vault_bp.route("/download/<int:file_id>", methods=["GET"])
@require_auth
def download_file(file_id):
    vf = VaultFile.query.get(file_id)
    if not vf:
        return jsonify({"error": "File not found"}), 404
    file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], vf.filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File missing on server"}), 404

    with open(file_path, "rb") as f:
        decrypted = decrypt_file(f.read())

    return (
        decrypted,
        200,
        {
            "Content-Disposition": f'attachment; filename="{vf.original_name}"',
            "Content-Type": vf.mime_type
        }
    )
