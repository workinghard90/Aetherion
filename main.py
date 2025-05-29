from aetherion import create_app
from aetherion.extensions import db
from aetherion.models import User, Document

app = create_app()

# Optional: shell context for `flask shell`
@app.shell_context_processor
def make_shell_context():
    return {
        "app": app,
        "db": db,
        "User": User,
        "Document": Document,
    }

if __name__ == "__main__":
    import os
    app.run(
        debug=os.getenv("FLASK_ENV") == "development",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
