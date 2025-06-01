# Aetherion/backend/aetherion/auth_middleware.py

from functools import wraps
from flask import request, jsonify, g
from .auth import decode_token

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]
        try:
            user_data = decode_token(token)
            g.user = user_data
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 403

        return f(*args, **kwargs)
    return decorated


def try_auth():
    """Optional auth – silently attach user if token is valid."""
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            user_data = decode_token(token)
            g.user = user_data
        except Exception:
            g.user = None
    else:
        g.user = None
