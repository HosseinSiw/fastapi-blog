from utils.jwt import verify_access_token, oauth2_schema
from db.session import SessionLocal
from fastapi import Depends, HTTPException


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close() 
        
        
def get_current_user(token: str = Depends(oauth2_schema)):
    payload  = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Invalid token')
    
    return payload