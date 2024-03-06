from fastapi import FastAPI
from database.database import engine
from database.database import Base
from routes.router import router
app = FastAPI()

Base.metadata.create_all(bind = engine)

 
@app.get("/")
async def root():
    return {"message": "Hellooo !!!!"}

app.include_router(router,prefix="/users", tags=["user"])