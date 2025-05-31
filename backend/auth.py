import os
import jwt
from functools import wraps
from flask import request, jsonify, g
from models import User
from extensions import db

SECRET_KEY = os.getenv("SECRET_KEY", "change-me")

def generate_token(user_id):
    payload = {"user_id": user_id}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload  # e.g. {"user_id": 1}

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]
        try:
            payload = decode_token(token)
            user = User.query.get(payload.get("user_id"))
            if not user:
                raise Exception("User not found")
            g.user = user
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 403
        return f(*args, **kwargs)
    return decorated

def try_auth():
    """Silently attach user if token valid, else g.user = None."""
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            payload = decode_token(token)
            g.user = User.query.get(payload.get("user_id"))
        except:
            g.user = None
    else:
        g.user = None
