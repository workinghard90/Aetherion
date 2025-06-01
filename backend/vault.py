# Aetherion/backend/aetherion/routes.py

from flask import Blueprint, request, jsonify, g, current_app, send_file
from .extensions import db
from .models import User, VaultFile
from .auth import authenticate, create_user
from .auth_middleware import require_auth, try_auth
from .crypto import decrypt_file
import os

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
# ─── VAULT ENDPOINTS ───────────────────────────────────────────────────────────
#

from .vault import vault_bp
api_bp.register_blueprint(vault_bp, url_prefix="/vault")


#
# ─── SCROLLS / ARCHIVE ─────────────────────────────────────────────────────────
#

@api_bp.route("/archive", methods=["GET"])
@try_auth
def list_archive():
    """
    Returns list of all archived scrolls/files (metadata), optionally with content
    if the user is authenticated and allowed. 
    """
    # If a user is logged in, we can return their files; otherwise just metadata.
    user = getattr(g, "user", None)
    files = VaultFile.query.all()
    return jsonify([f.to_dict() for f in files]), 200


@api_bp.route("/archive/<int:file_id>", methods=["GET"])
@try_auth
def get_scroll(file_id):
    """
    If a user is authenticated, we decrypt and send the file contents.
    Otherwise we just respond with metadata.
    """
    vf = VaultFile.query.get_or_404(file_id)
    user = getattr(g, "user", None)
    if user and user["user_id"] == vf.user_id:
        path = os.path.join(current_app.config["UPLOAD_FOLDER"], vf.filename)
        with open(path, "rb") as f:
            decrypted = decrypt_file(f.read())
        # Return the decrypted bytes with correct mime type
        return send_file(
            io.BytesIO(decrypted), 
            download_name=vf.original_name, 
            mimetype=vf.mime_type
        )
    else:
        # Not allowed or not authenticated: return metadata only
        return jsonify(vf.to_dict()), 200


#
# ─── ORACLE ENDPOINT (Chatbot) ──────────────────────────────────────────────────
#

@api_bp.route("/oracle", methods=["POST"])
@try_auth       # Will still work if not logged in; g.user will be None
def oracle_chat():
    data = request.json or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Dummy placeholder: you should hook this into your actual LLM/transformers pipeline
    answer = f"Grove says: I hear you asking '{question}'. I am still learning to answer."
    return jsonify({"answer": answer}), 200
