import os
from flask import Flask
from flask_cors import CORS
from extensions import db, migrate
from routes import api_bp

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile("config.json")
    # Load environment variables from .env if present
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

    # Override config from environment
    app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER", app.config["UPLOAD_FOLDER"])
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", app.config["SQLALCHEMY_DATABASE_URI"])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix="/api")
    return app

app = create_app()

if __name__ == "__main__":
    # Create tables and run
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
