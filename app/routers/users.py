from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from schemas.users import UserRetriveSchema, UserCreationSchmea
from .dependencies import get_db
from sqlalchemy.orm import Session
from models.user import User as UserTable
from utils.passwords import hash_password, verify_password
from utils.jwt import create_access_token, verify_access_token, get_current_user


router = APIRouter(prefix='/users', tags=['users',])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/register", response_model=UserRetriveSchema)
def register_new_user(user: UserCreationSchmea, db: Session = Depends(get_db)):
    existing_user = db.query(UserTable,).filter(UserTable.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail={"Error": "the provided email has already exists"})
    
    user.password = hash_password(user.password)
    new_user = UserTable(email=user.email, name=user.name, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login_jwt(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserTable).filter(UserTable.email == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={'sub': str(user.email + " " + user.name)},)
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
