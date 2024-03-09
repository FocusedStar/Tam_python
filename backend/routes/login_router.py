from fastapi import APIRouter, HTTPException, Path, Depends,Body
from database.database import SessionLocal
from sqlalchemy.orm import Session 
from schemas.user_schema import RequestUser, User_schema, UserLogin_schema
from schemas.response_schema import Response
from crud import user_crud
from authentication.jwt_handler import signJWT

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@router.post("/login",tags=["user"])
def check_user(data: UserLogin_schema, db: Session = Depends(get_db)):
   correct_credentials =  user_crud.check_user(db,user_email=data.email,user_password=data.password)

   if correct_credentials: return signJWT(data.email)