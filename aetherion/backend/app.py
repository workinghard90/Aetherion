from flask import Flask
from .config import Config
from .extensions import init_extensions, db
from .routes import api_bp
from .health import health_bp
from .vault import vault_bp  # import vault

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    init_extensions(app)

    # Create tables (if using SQLite)
// Note: in production, use migrations instead
    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(vault_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(__import__("os").environ.get("PORT", 5000)),
        debug=app.config["DEBUG"],
    )
