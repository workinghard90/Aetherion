from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os

class EncryptionService:
    def __init__(self, password: str):
        salt = b"AetherionSalt"
        self.key = PBKDF2(password, salt, dkLen=32, count=1000000)

    def encrypt(self, data: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return iv + tag + ciphertext

    def decrypt(self, token: bytes) -> bytes:
        iv = token[:16]
        tag = token[16:32]
        ciphertext = token[32:]
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=iv)
        return cipher.decrypt_and_verify(ciphertext, tag)
