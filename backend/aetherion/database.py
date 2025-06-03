from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

def get_engine():
    # Example: use the same DATABASE_URL environment variable
    db_url = os.getenv("DATABASE_URL", "sqlite:///aetherion.db")
    return create_engine(db_url)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
