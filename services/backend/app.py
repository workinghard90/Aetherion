# services/backend/app.py

from flask import Flask, jsonify
from routes.docs import docs
from routes.gates import gates
from routes.veil import veil

app = Flask(__name__)
app.register_blueprint(docs)
app.register_blueprint(gates)
app.register_blueprint(veil)

@app.route("/aetherion/arrival")
def arrival():
    return {"message": "Welcome Guardian", "pulse": "aligned"}

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Aetherion API is live.",
        "status": "AetherionAI API is live.",
        "routes": [
            "/api",
            "/docs",
            "/api/items",
            "/aetherion/arrival",
            "/aetherion/gate/becoming"
        ]
    }), 200

if __name__ == "__main__":
    app.run(port=10000)
