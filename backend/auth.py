from functools import wraps
from flask import request, jsonify, g
import jwt
import os
from datetime import datetime, timedelta

# Replace this with your own secret / JWT logic
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

def encode_token(user_id):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=24),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

def require_auth(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401
        token = auth_header.split(" ")[1]
        try:
            user_data = decode_token(token)
            g.user_id = user_data["sub"]
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 403
        return fn(*args, **kwargs)
    return wrapper

def try_auth():
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            user_data = decode_token(token)
            g.user_id = user_data["sub"]
        except Exception:
            g.user_id = None
    else:
        g.user_id = None
