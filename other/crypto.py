import hashlib
import secrets


def generatePasswordHash(password : str) -> str:
    blake = hashlib.blake2s()
    blake.update(password.encode())
    salt = secrets.token_hex(8)
    blake.update(salt.encode())
    return blake.hexdigest() + ":" + salt

def verifyPasswordHash(password : str, passwordstore : str) -> bool:
    blake = hashlib.blake2s()
    blake.update(password.encode())
    blake.update(passwordstore.split(":")[1].encode())
    return blake.hexdigest() == passwordstore.split(":")[0]