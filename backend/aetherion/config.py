import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class AetherionConfig:
    DATA_PATH = BASE_DIR / "data"
    LOG_PATH = BASE_DIR / "logs"
