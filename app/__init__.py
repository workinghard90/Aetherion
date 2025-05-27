```python
from .auth import auth_bp
from .vault import vault_bp
from .health import health_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vault_bp, url_prefix="/vault")
    app.register_blueprint(health_bp)
```
