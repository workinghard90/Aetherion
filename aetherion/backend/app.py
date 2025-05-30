from flask import Flask
from .extensions import init_extensions
from .routes import api_bp
from .health import health_bp

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("backend.config.Config")
    init_extensions(app)
    app.register_blueprint(api_bp)
    app.register_blueprint(health_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT",5000)))
