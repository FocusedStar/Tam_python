from fastapi import APIRouter, HTTPException, Path, Depends,Body
from database.database import SessionLocal
from sqlalchemy.orm import Session 
from schemas.user_schema import RequestUser, User_schema, UserLogin_schema
from schemas.response_schema import Response
from crud import user_crud, permission_crud
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
   _user=  user_crud.check_user(db,user_email=data.email,user_password=data.password)

   if _user: 
      _permissions = permission_crud.get_permissions_list(db=db, _permissionsList=_user.permissions)
      return signJWT(_user,_permissions)