from fastapi import FastAPI, Depends
from database.database import engine,Base
from routes import user_router,login_router, permissions_router
from authentication.jwt_bearer import jwtBearer

app = FastAPI()

Base.metadata.create_all(bind = engine)

 
@app.get("/",dependencies=[Depends(jwtBearer)])
async def root():
    return {"message": "Hellooo !!!!"}

app.include_router(user_router.router,prefix="/users", dependencies=[Depends(jwtBearer())], tags=["user"])
app.include_router(login_router.router,prefix="/users", dependencies=[Depends(jwtBearer())], tags=["user"])
app.include_router(permissions_router.router,prefix="/managment", dependencies=[Depends(jwtBearer())], tags=["Permissions"])