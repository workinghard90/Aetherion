import os
import json
import sqlite3
import zipfile
import tempfile
import io
from flask import Blueprint, jsonify, request, send_file

docs = Blueprint("docs", __name__)
DB_PATH = os.environ.get("DATABASE_URL", "universe.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_doc_table():
    db = get_db()
    db.execute('''
    CREATE TABLE IF NOT EXISTS aetherion_docs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        summary TEXT,
        full_content TEXT,
        source TEXT DEFAULT 'manual',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    db.execute('''
    CREATE TABLE IF NOT EXISTS scroll_import_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        status TEXT,
        detail TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    db.commit()
    db.close()

@docs.before_app_first_request
def setup_docs():
    init_doc_table()

@docs.route("/api/docs", methods=["GET"])
def list_docs():
    db = get_db()
    rows = db.execute("SELECT name, summary FROM aetherion_docs ORDER BY created_at DESC").fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])

@docs.route("/api/docs/<name>", methods=["GET"])
def get_doc(name):
    db = get_db()
    row = db.execute("SELECT * FROM aetherion_docs WHERE name = ?", (name,)).fetchone()
    db.close()
    if not row:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))

@docs.route("/api/docs", methods=["POST"])
def upload_doc():
    data = request.get_json()
    source = data.get("source", "manual")
    db = get_db()
    db.execute(
        "INSERT INTO aetherion_docs (name, summary, full_content, source) VALUES (?, ?, ?, ?)",
        (data["name"], data["summary"], json.dumps(data["full_content"]), source)
    )
    db.commit()
    db.close()
    return jsonify({"status": "stored", "source": source})

@docs.route("/api/docs/download/<name>", methods=["GET"])
def download_doc(name):
    db = get_db()
    row = db.execute("SELECT full_content FROM aetherion_docs WHERE name = ?", (name,)).fetchone()
    db.close()
    if not row:
        return jsonify({"error": "Not found"}), 404
    content = json.loads(row["full_content"])
    filename = f"{name.replace(' ', '_').lower()}.json"
    return jsonify(content), 200, {
        'Content-Disposition': f'attachment; filename="{filename}"',
        'Content-Type': 'application/json'
    }

@docs.route("/api/docs/download/all", methods=["GET"])
def download_all_scrolls():
    db = get_db()
    rows = db.execute("SELECT name, full_content FROM aetherion_docs").fetchall()
    db.close()
    if not rows:
        return jsonify({"error": "No scrolls available."}), 404
    memory = io.BytesIO()
    with zipfile.ZipFile(memory, "w") as zipf:
        for row in rows:
            name = row["name"].replace(" ", "_").lower()
            content = json.loads(row["full_content"])
            zipf.writestr(f"{name}.json", json.dumps(content, indent=2))
    memory.seek(0)
    return send_file(
        memory,
        download_name="aetherion_scrolls.zip",
        as_attachment=True,
        mimetype="application/zip"
    )

@docs.route("/api/docs/upload/batch", methods=["POST"])
def upload_scroll_batch():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if not file.filename.endswith('.zip'):
        return jsonify({"error": "Only .zip files accepted"}), 400
    override_source = request.args.get("source", "batch")
    rejected_scrolls = []
    imported_files = []

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, file.filename)
        file.save(zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            db = get_db()
            for name in zipf.namelist():
                if not name.endswith(".json"):
                    continue
                raw = zipf.read(name).decode("utf-8")
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                required_fields = {"name", "type"}
                missing_fields = required_fields - data.keys()
                if missing_fields:
                    db.execute(
                        "INSERT INTO scroll_import_log (filename, status, detail) VALUES (?, ?, ?)",
                        (name, "rejected", json.dumps(list(missing_fields)))
                    )
                    rejected_scrolls.append({
                        "file": name,
                        "missing": list(missing_fields)
                    })
                    continue
                base_name = os.path.splitext(os.path.basename(name))[0].replace("_", " ").title()
                db.execute(
                    "INSERT INTO aetherion_docs (name, summary, full_content, source) VALUES (?, ?, ?, ?)",
                    (base_name, f"Imported scroll: {base_name}", json.dumps(data), override_source)
                )
                db.execute(
                    "INSERT INTO scroll_import_log (filename, status, detail) VALUES (?, ?, ?)",
                    (name, "imported", "")
                )
                imported_files.append(name)
            db.commit()
            db.close()

    return jsonify({
        "status": "batch import complete",
        "imported": imported_files,
        "rejected": rejected_scrolls
    })

@docs.route("/api/docs/web", methods=["GET"])
def serve_web_docs():
    return send_file("docs/index.html")
