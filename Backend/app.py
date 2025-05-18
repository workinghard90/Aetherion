from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3, json, os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_PATH = os.environ.get("DATABASE_URL", "universe.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
      CREATE TABLE IF NOT EXISTS universe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type TEXT,
        description TEXT,
        properties TEXT,
        created_at TEXT
      )
    ''')
    conn.commit()
    conn.close()

@app.route("/api/items", methods=["GET"])
def list_items():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM universe").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM universe WHERE id=?", (item_id,)).fetchone()
    conn.close()
    if not row:
        return jsonify({"error":"Not found"}), 404
    return jsonify(dict(row))

@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute(
      "INSERT INTO universe (name,type,description,properties,created_at) VALUES (?,?,?,?,?)",
      (
        data.get("name"),
        data.get("type"),
        data.get("description",""),
        json.dumps(data.get("properties",{})),
        datetime.utcnow().isoformat()
      )
    )
    conn.commit()
    conn.close()
    return jsonify({"status":"created"}), 201

@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    conn = get_db_connection()
    conn.execute(
      "UPDATE universe SET name=?,type=?,description=?,properties=? WHERE id=?",
      (
        data.get("name"),
        data.get("type"),
        data.get("description",""),
        json.dumps(data.get("properties",{})),
        item_id
      )
    )
    conn.commit()
    conn.close()
    return jsonify({"status":"updated"})

@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM universe WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return jsonify({"status":"deleted"})

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
