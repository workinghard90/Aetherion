# backend/app.py

import os
from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .config import Config
from .routes import main_bp
from .vault import vault_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    # Initialize database & migrations
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints under `/api` prefix
    app.register_blueprint(main_bp, url_prefix="/api")
    app.register_blueprint(vault_bp, url_prefix="/api/vault")

    # Create tables if they don’t exist
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host="0.0.0.0", port=port, debug=True)
