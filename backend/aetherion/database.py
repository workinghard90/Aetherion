# Aetherion/backend/aetherion/database.py

# This file can contain any database utility functions. For now, it's a placeholder.

from .extensions import db

def init_db():
    db.create_all()
