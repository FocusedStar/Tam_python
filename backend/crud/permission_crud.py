from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from  models.user_model import Permission
from schemas.permission_schema import Permission_schema
from typing import List

def create_permission(db:Session, input_user:Permission_schema):
    _permission = Permission(permission=input_user.permission)
    
    try:
        db.add(_permission)
        db.commit()
        db.refresh(_permission)
        return _permission
    except:
         raise HTTPException(status_code=409, detail="Error Creating Element")
    
def get_permissions(db: Session, skip:int=0, limit:int=100):
    return db.query(Permission).offset(skip).limit(limit).all()


def get_permission_by_id(db: Session, permission_id: int):
    return db.query(Permission).filter(Permission.id == permission_id).first()

def get_permissions_list(db: Session, _permissionsList: List[str]):
    try:
        _permissons = db.execute(select(Permission.permission).filter(Permission.id.in_(_permissionsList))).scalars().all()
        print (_permissons)
        return _permissons
    except:
        raise HTTPException(status_code=500, detail="Error Getting Elements")
                         