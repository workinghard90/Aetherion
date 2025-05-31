import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
from .health import health_bp
app.register_blueprint(health_bp)


# 1) Load .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

# 2) Create Flask app
app = Flask(__name__)

# 3) Load config from config.py
app.config.from_object("config.Config")

# 4) Enable CORS
CORS(app)

# 5) Initialize DB extensions
from .extensions import db, migrate
db.init_app(app)
migrate.init_app(app, db)

# 6) Register models and blueprints
#     Universe and VaultFile models are registered via SQLAlchemy when we import them below.
from .models.universe import Universe
from .models.file import VaultFile

from .routes import api_bp
app.register_blueprint(api_bp)

# 7) Register health or other views if needed
#    e.g.: from .health import health_bp
#          app.register_blueprint(health_bp)

if __name__ == "__main__":
    # On local dev, run with Flask dev server
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
