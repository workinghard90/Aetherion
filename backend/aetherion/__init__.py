# Aetherion/backend/aetherion/__init__.py

import os
from flask import Flask
from .extensions import db, migrate
from .routes import api_bp
from dotenv import load_dotenv

# Load .env locally (but on Render, it uses real environment variables).
load_dotenv(os.path.join(os.path.dirname(__file__), os.pardir, ".env"))

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # 1) Load config.json (base configuration)
    #    Then override with any environment variables set (Render will provide DATABASE_URL, SECRET_KEY, etc.)
    app.config.from_file("config.json", load=json_load)
    app.config.from_prefixed_env()  # a Flask 2.3+ method: loads env vars matching uppercase config keys

    # 2) Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # 3) Register Blueprints
    app.register_blueprint(api_bp, url_prefix="/api")

    # 4) Basic health check endpoint
    @app.route("/healthz")
    def healthz():
        return {"status": "ok"}, 200

    return app


# Because Flask's load_json (from_file) expects a Python function that loads JSON:
def json_load(file_path):
    import json
    return json.load(open(file_path))
