# services/backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Blueprint imports
from routes.docs import docs
from routes.gates import gates
from routes.veil import veil

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register Blueprints
    app.register_blueprint(docs)
    app.register_blueprint(gates)
    app.register_blueprint(veil)

    @app.route("/aetherion/arrival")
    def arrival():
        return {
            "message": "Welcome Guardian",
            "pulse": "aligned"
        }

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

    return app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
