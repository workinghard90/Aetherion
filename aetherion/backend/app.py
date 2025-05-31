# backend/app.py

import os
import json
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# ─────────────────────────────────────────────────────────────────────────────
# 1) Load environment variables from .env (if present)
# ─────────────────────────────────────────────────────────────────────────────
load_dotenv()  # will look for a "backend/.env" automatically

# ─────────────────────────────────────────────────────────────────────────────
# 2) Flask and Extension Initialization
# ─────────────────────────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)

# By default, use a local SQLite DB file called "universe.db" unless overridden:
db_url = os.getenv("DATABASE_URL", "sqlite:///universe.db")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# ─────────────────────────────────────────────────────────────────────────────
# 3) Define Your Model(s)
# ─────────────────────────────────────────────────────────────────────────────
class Universe(db.Model):
    __tablename__ = "universe"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    properties = db.Column(db.Text, nullable=True)  # JSON as text
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "properties": json.loads(self.properties or "{}"),
            "created_at": self.created_at.isoformat(),
        }


# ─────────────────────────────────────────────────────────────────────────────
# 4) API Endpoints
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/items", methods=["GET"])
def get_items():
    items = Universe.query.all()
    return jsonify([item.to_dict() for item in items]), 200


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Universe.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item.to_dict()), 200


@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json() or {}
    name = data.get("name")
    type_ = data.get("type")
    description = data.get("description", "")
    properties = data.get("properties", {})

    if not name or not type_:
        return jsonify({"error": "name and type are required"}), 400

    new_item = Universe(
        name=name,
        type=type_,
        description=description,
        properties=json.dumps(properties),
    )
    db.session.add(new_item)
    db.session.commit()

    return jsonify({"status": "created", "id": new_item.id}), 201


@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json() or {}
    item = Universe.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404

    item.name = data.get("name", item.name)
    item.type = data.get("type", item.type)
    item.description = data.get("description", item.description)
    item.properties = json.dumps(data.get("properties", json.loads(item.properties)))

    db.session.commit()
    return jsonify({"status": "updated"}), 200


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Universe.query.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"status": "deleted"}), 200


# ─────────────────────────────────────────────────────────────────────────────
# 5) If run directly, start Flask
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Running "flask run" or "python app.py" will both work.
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
