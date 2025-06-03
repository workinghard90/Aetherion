from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models import File, db
from io import BytesIO
from datetime import datetime

vault_bp = Blueprint("vault", __name__)

@vault_bp.route("/upload", methods=["POST"])
@jwt_required()
def upload():
    user_id = get_jwt_identity()
    file = request.files["file"]

    new_file = File(
        original_name=file.filename,
        user_id=user_id,
        uploaded_at=datetime.utcnow(),
        blob=file.read()
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify(message="File uploaded successfully"), 201

@vault_bp.route("/list", methods=["GET"])
@jwt_required()
def list_files():
    user_id = get_jwt_identity()
    files = File.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": f.id,
        "original_name": f.original_name,
        "uploaded_at": f.uploaded_at.isoformat(),
        "user_id": f.user_id
    } for f in files])

@vault_bp.route("/download/<int:file_id>", methods=["GET"])
@jwt_required()
def download(file_id):
    file = File.query.get_or_404(file_id)
    return send_file(BytesIO(file.blob), download_name=file.original_name, as_attachment=True)
