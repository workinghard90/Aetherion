from flask import Blueprint, request, jsonify, g
from extensions import db
from models import User
from auth import generate_token, require_auth, try_auth
from vault import vault_bp

api_bp = Blueprint("api_bp", __name__)

# Register vault blueprint under /api
api_bp.register_blueprint(vault_bp)

# --- Authentication Routes ---

@api_bp.route("/auth/register", methods=["POST"])
def register():
    data = request.json or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username & password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    from werkzeug.security import generate_password_hash
    new_user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    token = generate_token(new_user.id)
    return jsonify({"message": "User created", "token": token}), 201

@api_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.json or {}
    username = data.get("username")
    password = data.get("password")
    from werkzeug.security import check_password_hash
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401
    token = generate_token(user.id)
    return jsonify({"message": "Login successful", "token": token})

# --- Universe “items” endpoints (simple example) ---

@api_bp.route("/items", methods=["GET"])
@require_auth
def get_items():
    from datetime import datetime
    # Example static data; in practice you’d fetch from DB
    sample = [
        {"id": 1, "name": "Star Alpha", "type": "Star", "description": "A bright star", "created_at": datetime.utcnow().isoformat()},
        {"id": 2, "name": "Planet Beta", "type": "Planet", "description": "A rocky planet", "created_at": datetime.utcnow().isoformat()}
    ]
    return jsonify(sample)

@api_bp.route("/items/<int:item_id>", methods=["GET"])
@require_auth
def get_item(item_id):
    # Dummy response
    return jsonify({"id": item_id, "name": f"Entity {item_id}", "type": "Unknown", "description": "Details here"})

@api_bp.route("/items", methods=["POST"])
@require_auth
def create_item():
    data = request.json or {}
    # Dummy create
    return jsonify({"message": "Created", "data": data}), 201

@api_bp.route("/items/<int:item_id>", methods=["PUT"])
@require_auth
def update_item(item_id):
    data = request.json or {}
    # Dummy update
    return jsonify({"message": f"Item {item_id} updated", "data": data})

@api_bp.route("/items/<int:item_id>", methods=["DELETE"])
@require_auth
def delete_item(item_id):
    # Dummy delete
    return jsonify({"message": f"Item {item_id} deleted"})
