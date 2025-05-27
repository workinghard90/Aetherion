# services/backend/veil_of_the_grove.py

from app import create_app
from flask_cors import CORS
import os

app = create_app()
CORS(app)

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_ENV", "production") == "development"
    app.run(debug=debug_mode, host="0.0.0.0", port=5000)
