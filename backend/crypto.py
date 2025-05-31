from cryptography.fernet import Fernet
import os

# You can store your key in an environment variable for production
KEY = os.getenv("ENCRYPTION_KEY", None)
if not KEY:
    # Generate a key if not provided (development only)
    KEY = Fernet.generate_key().decode()
    os.environ["ENCRYPTION_KEY"] = KEY

f = Fernet(KEY)

def encrypt_file(data: bytes) -> bytes:
    return f.encrypt(data)

def decrypt_file(token: bytes) -> bytes:
    return f.decrypt(token)
