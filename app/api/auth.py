from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from aetherion.models.user import User
from aetherion.extensions import db
from aetherion.core.auth import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "User already exists"}), 409

    hashed = generate_password_hash(data["password"])
    new_user = User(username=data["username"], password=hashed)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user.id)
    return jsonify({"token": token})
