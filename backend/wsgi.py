---

### `backend/app.py`
```python
import os
from flask import Flask
from .config import Config
from .extensions import db, migrate, cors, jwt
from .routes import register_routes
from .health import bp as health_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(health_bp, url_prefix="/health")
    register_routes(app)

    return app

app = create_app()
