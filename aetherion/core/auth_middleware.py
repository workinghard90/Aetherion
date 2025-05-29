from functools import wraps
from flask import request, jsonify
from aetherion.core.auth import decode_token  # your existing function

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]
        try:
            user_data = decode_token(token)
            request.user = user_data  # inject user into request context
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 403

        return f(*args, **kwargs)
    return decorated
