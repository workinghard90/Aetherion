import os

class Config:
    DEBUG = False
    # Database URL (Render will set DATABASE_URL; otherwise local sqlite)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{os.getcwd()}/universe.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Folder where encrypted uploads are stored
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(os.getcwd(), "uploads"))
