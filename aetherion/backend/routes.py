from flask import Blueprint, jsonify, request
from .database import get_db_connection, init_db
import json
from datetime import datetime

api_bp = Blueprint("api", __name__, url_prefix="/api")

# Initialize DB
init_db()

# Items endpoints
@api_bp.route("/items", methods=["GET"])
def list_items():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM universe").fetchall()
    conn.close()
    return jsonify([dict(r) for r in items])

@api_bp.route("/items/<int:id>", methods=["GET"])
def get_item(id):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM universe WHERE id=?", (id,)).fetchone()
    conn.close()
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(item))

@api_bp.route("/items", methods=["POST"])
def create_item():
    data = request.json
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO universe (name,type,description,properties,created_at) VALUES (?,?,?,?,?)",
        (data["name"], data["type"], data.get("description",""),
         json.dumps(data.get("properties",{})), datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()
    return jsonify({"status":"created"}), 201

# Scrolls endpoint (initial JSON archives)
@api_bp.route("/scrolls", methods=["GET"])
def list_scrolls():
    # load all .json in backend/archives/
    import glob, os
    archives = []
    for path in glob.glob("backend/*.json"):
        with open(path) as f:
            archives.append(json.load(f))
    return jsonify(archives)
