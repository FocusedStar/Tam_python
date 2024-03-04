from fastapi import APIRouter, HTTPException, Path, Depends
from database.database import SessionLocal
from sqlalchemy.orm import Session 
from schemas.user_schema import RequestUser
from schemas.response_schema import Response
from crud import user_crud


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_user")
async def create_user(request: RequestUser,db: Session=Depends(get_db)):
    user_crud.create_user(db,input_user= request.parameter)
    return Response(code=200,status="OK", message="Record created successfully").dict(exclude_none = True)


@router.get("/get_user")
async def get_user(db: Session=Depends(get_db)):
    _user = user_crud.get_user(db,0,100)
    if not _user:
        raise HTTPException(status_code=404, detail="Record not found")
    return Response(code=200,status="OK", message="Record Fetched successfully", result=_user).dict(exclude_none = True)
@router.get("/{id}")
async def get_user_by_id(id:int,db: Session=Depends(get_db)):
    _user = user_crud.get_user_by_id(db, id)
    if not _user:
        raise HTTPException(status_code=404, detail="Record not found")
    return Response(code=200,status="OK", message="Record Fetched successfully", result=_user).dict(exclude_none = True)

@router.post("/update_user")
async def update_user(request: RequestUser,db: Session=Depends(get_db)):
    _user = user_crud.update_user(db,user_id=request.parameter.id, input_user_name=request.parameter.name)
    return Response(code=200,status="OK", message="Record updated successfully", result=_user).dict(exclude_none = True)

@router.delete("/{id}")
async def delete_user(id:int,db: Session=Depends(get_db)):
    _user = user_crud.remove_user(db, id)
    if not _user:
        raise HTTPException(status_code=404, detail="Record not found")
    return Response(code=200,status="OK", message="Record Deleted successfully").dict(exclude_none = True)
