from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("HASH_ALGORITHM")


ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict,):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire time": expire})
    token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    print('Token:', token)
    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM,])
        return payload
    except JWTError:
        return None
    
    
def get_current_user(token: str = Depends(oauth2_schema)):
    payload  = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Invalid token')
    
    return payload