from flask import Blueprint, jsonify, request, g
from .database import get_db_connection, init_db
from .auth import require_auth, try_auth
import json
from datetime import datetime

api_bp = Blueprint("api", __name__, url_prefix="/api")

# Initialize DB once on import
init_db()

@api_bp.before_request
def attach_optional_user():
    try_auth()

@api_bp.route("/items", methods=["GET"])
def list_items():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM universe").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@api_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM universe WHERE id=?", (item_id,)).fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))

@api_bp.route("/items", methods=["POST"])
@require_auth
def create_item():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO universe (name,type,description,properties,created_at) VALUES (?,?,?,?,?)",
        (
            data["name"],
            data["type"],
            data.get("description", ""),
            json.dumps(data.get("properties", {})),
            datetime.utcnow().isoformat(),
        ),
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "created"}), 201

@api_bp.route("/items/<int:item_id>", methods=["PUT"])
@require_auth
def update_item(item_id):
    data = request.get_json()
    conn = get_db_connection()
    conn.execute(
        "UPDATE universe SET name=?, type=?, description=?, properties=? WHERE id=?",
        (
            data["name"],
            data["type"],
            data.get("description", ""),
            json.dumps(data.get("properties", {})),
            item_id,
        ),
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "updated"})

@api_bp.route("/items/<int:item_id>", methods=["DELETE"])
@require_auth
def delete_item(item_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM universe WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})
