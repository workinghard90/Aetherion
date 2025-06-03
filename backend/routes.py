from flask import Blueprint, request, jsonify
from .models import User, MemoryEntry, Scroll
from .extensions import db
from .auth_middleware import jwt_required

def register_routes(app):
    api_bp = Blueprint("api", __name__)

    @api_bp.route("/users", methods=["GET"])
    def get_users():
        users = User.query.all()
        return jsonify([{"id": u.id, "username": u.username} for u in users])

    @api_bp.route("/memories", methods=["POST"])
    @jwt_required
    def create_memory(user_id):
        data = request.get_json()
        entry = MemoryEntry(user_id=user_id, content=data.get("content"))
        db.session.add(entry)
        db.session.commit()
        return jsonify({"msg": "Memory created"}), 201

    @api_bp.route("/memories", methods=["GET"])
    @jwt_required
    def get_memories(user_id):
        entries = MemoryEntry.query.filter_by(user_id=user_id).all()
        return jsonify([{"id": e.id, "content": e.content, "created_at": e.created_at} for e in entries])

    @api_bp.route("/scrolls", methods=["GET"])
    def list_scrolls():
        scrolls = Scroll.query.all()
        return jsonify([{"id": s.id, "title": s.title} for s in scrolls])

    @api_bp.route("/scrolls/<int:id>", methods=["GET"])
    def get_scroll(id):
        s = Scroll.query.get_or_404(id)
        return jsonify({"id": s.id, "body": s.body})

    @api_bp.route("/scrolls", methods=["POST"])
    @jwt_required
    def create_scroll(user_id):
        data = request.get_json()
        s = Scroll(title=data.get("title"), body=data.get("body"))
        db.session.add(s)
        db.session.commit()
        return jsonify({"msg": "Scroll created"}), 201

    app.register_blueprint(api_bp, url_prefix="/api")
