from app import create_app
from flask_cors import CORS
import os

app = create_app()
CORS(app)

if __name__ == "__main__":
    is_debug = os.getenv("FLASK_ENV", "production") == "development"
    app.run(debug=is_debug, host="0.0.0.0", port=5000)
