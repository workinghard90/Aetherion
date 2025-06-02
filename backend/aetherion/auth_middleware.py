# backend/aetherion/auth_middleware.py
from functools import wraps
from flask import request, jsonify, g
import jwt
import os

# For simplicity, we’ll decode a JWT with a shared secret in ENV.
# In production, replace with your own decode logic.

SECRET_KEY = os.environ.get("JWT_SECRET", "CHANGE_ME_TO_A_REAL_SECRET")

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ", 1)[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            g.user = payload
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 403

        return f(*args, **kwargs)
    return decorated

def try_auth():
    """Optional auth middleware—no error if token missing or invalid."""
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header.split(" ", 1)[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            g.user = payload
        except Exception:
            g.user = None
    else:
        g.user = None
