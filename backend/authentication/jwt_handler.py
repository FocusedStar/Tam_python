# This file is responsible for signing, encodiing decoding and returning JWts

import time

from sqlalchemy import Null
from models.user_model import User
import jwt
from decouple import config
from typing import List, Dict
from crud.permission_crud import get_permissions_list
import json
JWT_SECRET_KEY = config('secret')
JWT_ALGORITHM = config('algorithem')

EXPIRY_TIME = 86400
def token_response(token: str):
    return {
        'access token': token,
        
    }

def signJWT(_user: User, _permission_list):
    # _permission_list = json.loads(_permission_list)
    print(f"List: {_permission_list}")
    payload = {
        "user_id": _user.id,
        "expiry": time.time() + EXPIRY_TIME,
        "permissions": _permission_list
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    print(f"Encoded: {token}")
    decodeJWT(token)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    
        print(f"{decode_token['permissions']}")
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        print("Invalid Token")