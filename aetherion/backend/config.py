import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE = os.getenv("DATABASE_URL", "universe.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
