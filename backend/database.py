# Optional: scripts for migrations or manual DB setup
from extensions import db
from models import User, VaultFile

def init_db():
    db.create_all()

if __name__ == "__main__":
    from app import app
    with app.app_context():
        init_db()
        print("Database initialized.")
