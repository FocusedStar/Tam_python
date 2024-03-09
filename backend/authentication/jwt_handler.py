# This file is responsible for signing, encodiing decoding and returning JWts

import time
import jwt
from decouple import config

JWT_SECRET_KEY = config('secret')
JWT_ALGORITHM = config('algorithem')

EXPIRY_TIME = 86400
def token_response(token: str):
    return {
        'access token': token,
        
    }

def signJWT(userID:str):
    payload = {
        "user_id": userID,
        "expiry": time.time() + EXPIRY_TIME
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}