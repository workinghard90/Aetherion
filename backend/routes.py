# backend/routes.py

import os
import json
from flask import Blueprint, request, jsonify, current_app, g
from werkzeug.utils import secure_filename
from app import db
from models import VaultFile, User
from auth import require_auth, try_auth
from crypto import encrypt_file, decrypt_file

api_bp = Blueprint("api", __name__)

# PUBLIC: get all items
@api_bp.route("/items", methods=["GET"])
def get_items():
    items = VaultFile.query.all()
    return jsonify([
        {
            "id": item.id,
            "filename": item.filename,
            "original_name": item.original_name,
            "mime_type": item.mime_type,
            "size": item.size,
            "user_id": item.user_id,
            "created_at": item.created_at.isoformat(),
        } for item in items
    ]), 200

# PUBLIC: get single item by ID
@api_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = VaultFile.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "id": item.id,
        "filename": item.filename,
        "original_name": item.original_name,
        "mime_type": item.mime_type,
        "size": item.size,
        "user_id": item.user_id,
        "created_at": item.created_at.isoformat(),
    }), 200

# PROTECTED: create/upload a new file
@api_bp.route("/items", methods=["POST"])
@require_auth
def upload_item():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)
    path = os.path.join(upload_folder, filename)

    # Encrypt the raw file bytes before saving
    encrypted_data = encrypt_file(file.read())
    with open(path, "wb") as f:
        f.write(encrypted_data)

    new_file = VaultFile(
        filename=filename,
        original_name=file.filename,
        mime_type=file.mimetype,
        size=len(encrypted_data),
        user_id=g.user["id"]  # assuming decode_token sets g.user to a dict with "id"
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded", "file_id": new_file.id}), 201

# PROTECTED: delete an item
@api_bp.route("/items/<int:item_id>", methods=["DELETE"])
@require_auth
def delete_item(item_id):
    item = VaultFile.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    if item.user_id != g.user["id"]:
        return jsonify({"error": "Forbidden"}), 403

    # Remove the file from disk
    file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], item.filename)
    if os.path.exists(file_path):
        os.remove(file_path)

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 200

# (Add further endpoints as needed…)
