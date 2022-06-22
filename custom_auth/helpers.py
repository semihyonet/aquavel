import hashlib
import time

import jwt

import aquavel.settings

def encrypt(value: str) -> str:
    return hashlib.md5(value.encode()).hexdigest()


def encode_jwt(value: str) -> str:
    return jwt.encode({"user_id": value, "id":1,"exp":int(time.time()+ 60 *60 * 24 *365)},
                      aquavel.settings.SECRET_KEY, algorithm="HS256")


def decode_jwt(value: str) -> dict:
    return jwt.decode(value, aquavel.settings.SECRET_KEY, algorithms=["HS256"],
                      options=dict(require = [], verify_signature=False) )
