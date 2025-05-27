```python
import os
from flask import Flask
from .config import get_config
from .extensions import db, migrate, cors
from .api import register_blueprints

def create_app():
    app = Flask(__name__)
    config = get_config(os.getenv("FLASK_ENV", "development"))
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    register_blueprints(app)
    return app
```
