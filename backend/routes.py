from flask import Blueprint, jsonify, request, g
from .models.universe import Universe
from .models.file import VaultFile
from .extensions import db
from .auth import require_auth, try_auth
import json
from datetime import datetime

main_bp = Blueprint("main", __name__)

@main_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK", "message": "Backend is alive!"})

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.before_request
def attach_optional_user():
    try_auth()

# --- CRUD: Universe Entities ---

@api_bp.route("/items", methods=["GET"])
def get_items():
    all_items = Universe.query.all()
    results = []
    for item in all_items:
        results.append({
            "id": item.id,
            "name": item.name,
            "type": item.type,
            "description": item.description,
            "properties": item.properties,
            "created_at": item.created_at.isoformat()
        })
    return jsonify(results), 200

@api_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Universe.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "id": item.id,
        "name": item.name,
        "type": item.type,
        "description": item.description,
        "properties": item.properties,
        "created_at": item.created_at.isoformat()
    }), 200

@api_bp.route("/items", methods=["POST"])
@require_auth
def create_item():
    data = request.json
    new_item = Universe(
        name=data["name"],
        type=data["type"],
        description=data.get("description", ""),
        properties=data.get("properties", {})
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"status": "created", "id": new_item.id}), 201

@api_bp.route("/items/<int:item_id>", methods=["PUT"])
@require_auth
def update_item(item_id):
    data = request.json
    item = Universe.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    item.name = data["name"]
    item.type = data["type"]
    item.description = data.get("description", "")
    item.properties = data.get("properties", {})
    db.session.commit()
    return jsonify({"status": "updated"}), 200

@api_bp.route("/items/<int:item_id>", methods=["DELETE"])
@require_auth
def delete_item(item_id):
    item = Universe.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({"status": "deleted"}), 200

# --- Vault (File Upload) ---

from werkzeug.utils import secure_filename
from flask import current_app
from .crypto import encrypt_file, decrypt_file

@api_bp.route("/vault/upload", methods=["POST"])
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

@api_bp.route("/vault/download/<int:file_id>", methods=["GET"])
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

# --- Health Check ---

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200
