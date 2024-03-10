from fastapi import APIRouter, HTTPException, Path, Depends
from database.database import SessionLocal
from sqlalchemy.orm import Session 
from schemas.permission_schema import RequestPermission
from schemas.response_schema import Response
from crud import permission_crud
from authentication.jwt_handler import signJWT
from authentication.jwt_bearer import jwtBearer

router = APIRouter()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@router.post("/create_permission")
async def create_permission(request: RequestPermission,db: Session=Depends(get_db)):
    permission_crud.create_permission(db,input_user= request.parameter)
    return Response(code=200,status="OK", message="Record created successfully").dict(exclude_none = True)


@router.get("/get_permissions")
async def get_user(db: Session=Depends(get_db)):
    _permissionList = permission_crud.get_permissions(db,0,100)
    if not _permissionList:
        raise HTTPException(status_code=404, detail="Record not found")
    return Response(code=200,status="OK", message="Record Fetched successfully", result=_permissionList).dict(exclude_none = True)
@router.get("/permission_by_id")
async def get_permission_by_id(id:int,db: Session=Depends(get_db)):
    _user = permission_crud.get_permission_by_id(db, id)
    if not _user:
        raise HTTPException(status_code=404, detail="Record not found")
    return Response(code=200,status="OK", message="Record Fetched successfully", result=_user).dict(exclude_none = True)




