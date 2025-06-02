# backend/aetherion/routes.py

import io
import os
from flask import Blueprint, request, jsonify, g, current_app, send_file
from .extensions import db
from .models import User, VaultFile
from .auth import authenticate, create_user
from .auth_middleware import require_auth, try_auth
from .crypto import decrypt_file
from .vault import vault_bp  # we register this blueprint below

api_bp = Blueprint("api", __name__)

#
# ─── AUTH ENDPOINTS ────────────────────────────────────────────────────────────
#

@api_bp.route("/auth/register", methods=["POST"])
def register():
    data = request.json or {}
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken"}), 400

    user = create_user(username, password)
    return jsonify({"message": "User created", "user_id": user.id}), 201


@api_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.json or {}
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    token = authenticate(username, password)
    if token:
        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


#
# ─── VAULT ENDPOINTS (Blueprint) ───────────────────────────────────────────────
#

# Register our vault blueprint under /api/vault
api_bp.register_blueprint(vault_bp, url_prefix="/vault")


#
# ─── ARCHIVE / SCROLLS (Optional Auth) ──────────────────────────────────────────
#

@api_bp.route("/archive", methods=["GET"])
def list_archive():
    """
    Returns list of all archived scrolls/files (metadata).
    If a valid token is provided, g.user will be set; otherwise g.user is None.
    """
    # Perform optional auth
    try_auth()

    files = VaultFile.query.all()
    return jsonify([f.to_dict() for f in files]), 200


@api_bp.route("/archive/<int:file_id>", methods=["GET"])
def get_scroll(file_id):
    """
    If the user is authenticated and owns the file, return decrypted contents.
    Otherwise return only metadata.
    """
    # Perform optional auth
    try_auth()

    vf = VaultFile.query.get_or_404(file_id)
    user = getattr(g, "user", None)

    # If user is logged in and owns this vault entry, send decrypted bytes
    if user and user["user_id"] == vf.user_id:
        path = os.path.join(current_app.config["UPLOAD_FOLDER"], vf.filename)
        if not os.path.exists(path):
            return jsonify({"error": "File missing on server"}), 404

        with open(path, "rb") as f:
            decrypted_bytes = decrypt_file(f.read())

        return send_file(
            io.BytesIO(decrypted_bytes),
            as_attachment=True,
            download_name=vf.original_name,
            mimetype=vf.mime_type
        )

    # Otherwise, return metadata only
    return jsonify(vf.to_dict()), 200


#
# ─── ORACLE ENDPOINT (Chatbot) ──────────────────────────────────────────────────
#

@api_bp.route("/oracle", methods=["POST"])
def oracle_chat():
    """
    Simple chatbot endpoint. Works whether or not user is logged in.
    """
    # Optional auth so that g.user is set if valid token exists
    try_auth()

    data = request.json or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Placeholder response
    answer = f"Grove says: I hear you asking '{question}'. I am still learning to answer."
    return jsonify({"answer": answer}), 200
