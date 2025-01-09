import hashlib

def password_hash(password: str):
    result = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return result
