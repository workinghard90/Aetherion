# services/backend/app/api/auth.py

from flask import Blueprint, request, jsonify
from ..models.user import User
from ..database import db
from ..services.auth import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if not data.get("username") or not data.get("password"):
        return {"error": "Username and password required"}, 400
    if User.query.filter_by(username=data["username"]).first():
        return {"error": "User exists"}, 400
    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered"}, 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not user.check_password(data["password"]):
        return {"error": "Invalid credentials"}, 401
    token = generate_token(user.id)
    return {"token": token}
