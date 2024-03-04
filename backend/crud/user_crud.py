from fastapi import HTTPException
from sqlalchemy.orm import Session
from  models.user_model import User
from schemas.user_schema import User_schema

def get_user(db: Session, skip:int=0, limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db:Session, input_user:User_schema):
    _user = User(name = input_user.name,job = input_user.job, email = input_user.email)
    try:
        db.add(_user)
        db.commit()
        db.refresh(_user)
        return _user
    except:
         raise HTTPException(status_code=409, detail="Error Creating Element")
        

def remove_user(db:Session, user_id:int):
    _user = get_user_by_id(db=db, user_id=user_id)
    try:
        db.delete(_user)
        db.commit()
    except:
        raise HTTPException(status_code=409, detail="Error Removing Element")


def update_user(db:Session, user_id:int,input_user_name:str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.name = input_user_name
    db.commit()
    db.refresh(_user)
    return _user