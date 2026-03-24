from cryptography.fernet import Fernet
import config

cipher = Fernet(config.SECRET_KEY.encode())

def encrypt(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt(data):
    return cipher.decrypt(data.encode()).decode()
