# backend/aetherion/routes.py
from flask import Blueprint, request, jsonify, g, send_file, current_app
from .extensions import db
from .models import User, VaultFile
from .auth_middleware import require_auth, try_auth
import io
import os
import jwt
from datetime import datetime, timedelta

api_bp = Blueprint("api", __name__)

SECRET_KEY = current_app.config.get("JWT_SECRET", "AUTUMN&CEALUM")

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

    # Simple (insecure) hashing for demonstration—swap for bcrypt or similar
    import hashlib
    pw_hash = hashlib.sha256(password.encode()).hexdigest()
    user = User(username=username, password_hash=pw_hash)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": user.id}), 201

@api_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.json or {}
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    import hashlib
    pw_hash = hashlib.sha256(password.encode()).hexdigest()
    user = User.query.filter_by(username=username, password_hash=pw_hash).first()
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate a short‐lived JWT:
    payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token}), 200

#
# ─── VAULT ENDPOINTS ───────────────────────────────────────────────────────────
#

# Import and register vault blueprint:
from .vault import vault_bp
api_bp.register_blueprint(vault_bp, url_prefix="/vault")

#
# ─── SCROLLS / ARCHIVE ENDPOINTS ────────────────────────────────────────────────
#

@api_bp.route("/archive", methods=["GET"])
@try_auth
def list_archive():
    """
    Return metadata for all archived files. If the user is authenticated,
    return their files; otherwise just metadata without download.
    """
    files = VaultFile.query.all()
    return jsonify([f.to_dict() for f in files]), 200

@api_bp.route("/archive/<int:file_id>", methods=["GET"])
@try_auth
def get_scroll(file_id):
    """
    If authenticated user owns this file, decrypt & send. Otherwise just metadata.
    """
    vf = VaultFile.query.get_or_404(file_id)
    user = getattr(g, "user", None)
    if user and user["user_id"] == vf.user_id:
        upload_dir = current_app.config["UPLOAD_FOLDER"]
        full_path = os.path.join(upload_dir, vf.filename)
        if not os.path.exists(full_path):
            return jsonify({"error": "File missing on server"}), 404
        with open(full_path, "rb") as f:
            decrypted = decrypt_file(f.read())
        return send_file(
            io.BytesIO(decrypted),
            download_name=vf.original_name,
            mimetype=vf.mime_type
        )
    else:
        return jsonify(vf.to_dict()), 200

#
# ─── ORACLE CHATBOT ENDPOINT ───────────────────────────────────────────────────
#

@api_bp.route("/oracle", methods=["POST"])
@try_auth
def oracle_chat():
    data = request.json or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Placeholder / stub answer:
    answer = f"Grove says: I hear you asking '{question}'. I am still learning to answer."
    return jsonify({"answer": answer}), 200
