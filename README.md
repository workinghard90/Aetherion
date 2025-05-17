from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/items", methods=["GET"])
def get_items():
    with open("config.json") as f:
        data = json.load(f)
    return jsonify({"items": data})

    {
  "entities": [
    { "name": "Caelum", "role": "Sky Architect" },
    { "name": "Autumn", "role": "Memory Weaver" }
  ]
}

FLASK_ENV=production
DATABASE_URL=sqlite:///db.sqlite3

web: gunicorn wsgi:app

Flask
gunicorn


from app import app

if __name__ == "__main__":
    app.run()

    
