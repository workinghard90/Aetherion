# Aetherion/backend/aetherion/scrolls.py

from flask import Blueprint, jsonify, request
from aetherion.models import File

scrolls_bp = Blueprint("scrolls", __name__)

@scrolls_bp.route("/", methods=["GET"])
def list_scrolls():
    files = File.query.all()
    return jsonify([{
        "id": f.id,
        "original_name": f.original_name,
        "uploaded_at": f.uploaded_at.isoformat(),
        "user_id": f.user_id
    } for f in files])

@scrolls_bp.route("/<int:file_id>", methods=["GET"])
def fetch_scroll(file_id):
    file = File.query.get_or_404(file_id)
    return file.blob  # or optionally send_file/BytesIO as download
