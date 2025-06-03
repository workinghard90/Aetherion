from flask import Blueprint, request, jsonify
from .models import MemoryEntry
from .extensions import db
from .auth_middleware import jwt_required
from .crypto import EncryptionService

bp = Blueprint("vault", __name__)
encryption = EncryptionService(password="vaultpassword")

@bp.route("/upload", methods=["POST"])
@jwt_required
def upload_memory(user_id):
    data = request.get_json()
    encrypted = encryption.encrypt(data.get("content").encode())
    entry = MemoryEntry(user_id=user_id, content=encrypted.hex())
    db.session.add(entry)
    db.session.commit()
    return jsonify({"msg": "Memory uploaded and encrypted"}), 201

@bp.route("/download/<int:id>", methods=["GET"])
@jwt_required
def download_memory(user_id, id):
    entry = MemoryEntry.query.filter_by(user_id=user_id, id=id).first_or_404()
    decrypted = encryption.decrypt(bytes.fromhex(entry.content)).decode()
    return jsonify({"content": decrypted}), 200
