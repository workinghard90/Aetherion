# backend/app.py
import os
from flask import Flask
from aetherion.extensions import db, migrate
from aetherion.routes import api_bp

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Load config.json
    app.config.from_file("config.json", load=lambda f: __import__("json").load(f))

    # Override with environment vars
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

    # Register blueprint(s)
    app.register_blueprint(api_bp, url_prefix="/api")

    # Create tables if not exist
    with app.app_context():
        db.create_all()

    return app

# Only used when running locally (python app.py)
if __name__ == "__main__":
    create_app().run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=app.config.get("DEBUG", False),
    )
