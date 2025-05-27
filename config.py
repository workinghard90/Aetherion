```python
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///vault.db")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 104857600))
    JWT_SECRET = os.getenv("JWT_SECRET", "dev_key")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

def get_config(env):
    return {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }.get(env, DevelopmentConfig)
```
