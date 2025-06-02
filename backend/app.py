# backend/app.py
import os
from flask import Flask
from aetherion.extensions import db, migrate
from aetherion.routes import api_bp

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Load config.json (must be valid Python syntax)
    app.config.from_file("config.json", load=lambda f: __import__("json").load(f))

    # Override with any env vars (optional)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", app.config["SQLALCHEMY_DATABASE_URI"]
    )
    app.config["JWT_SECRET"] = os.environ.get(
        "JWT_SECRET", app.config.get("JWT_SECRET")
    )
    app.config["UPLOAD_FOLDER"] = os.environ.get(
        "UPLOAD_FOLDER", app.config.get("UPLOAD_FOLDER", "uploads")
    )

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints under /api
    app.register_blueprint(api_bp, url_prefix="/api")

    # Create DB tables if they don't exist (useful in local or first‐time deploy)
    with app.app_context():
        db.create_all()

    return app

# If run directly (for local dev):
if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=app.config.get("DEBUG", False))
