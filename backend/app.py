# backend/app.py

import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load settings from config.py (must be valid Python)
    app.config.from_object("config")

    # Initialize CORS
    CORS(app)

    # Initialize database and migration engine
    db.init_app(app)
    migrate.init_app(app, db)

    # Make sure upload folder exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Register your Blueprints / routes here:
    from routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

# If you had a wsgi.py that does `from app import app`, 
# update it to call create_app()

if __name__ == "__main__":
    # On direct run, create the tables if needed and start the server
    app = create_app()

    # Ensure the database file / tables exist
    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
