# services/backend/app/__init__.py

from flask import Flask
from .database import db
from .api.vault import vault_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vault.db'
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .api.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

    app.register_blueprint(vault_bp, url_prefix="/vault")

    return app
