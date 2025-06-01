# Aetherion/backend/aetherion/auth.py

import os
import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .extensions import db

JWT_SECRET = os.getenv("JWT_SECRET", "default_jwt_secret")
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600  # 1 hour token validity

def create_user(username: str, password: str):
    """Helper to create a new user with a hashed password."""
    hashed = generate_password_hash(password)
    user = User(username=username, hashed_password=hashed)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate(username: str, password: str):
    """Check username/password. Returns JWT if valid, else None."""
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.hashed_password, password):
        payload = {
            "user_id": user.id,
            "username": user.username,
            "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token
    return None

def decode_token(token: str):
    """Decode and return user data from JWT."""
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return {
        "user_id": payload["user_id"],
        "username": payload["username"]
    }
