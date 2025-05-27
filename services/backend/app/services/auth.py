# services/backend/app/services/auth.py

import jwt
import datetime
from flask import current_app, request
from functools import wraps

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    secret = current_app.config["JWT_SECRET"]
    return jwt.encode(payload, secret, algorithm="HS256")

def decode_token(token):
    try:
        secret = current_app.config["JWT_SECRET"]
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return {"error": "Missing or invalid auth header"}, 401
        token = auth_header.split(" ")[1]
        data = decode_token(token)
        if not data:
            return {"error": "Invalid or expired token"}, 401
        request.user_id = data["user_id"]
        return f(*args, **kwargs)
    return decorated
