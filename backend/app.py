from fastapi import FastAPI
import psycopg2
import os
import base64
import datetime
from database.database import engine
from database.database import Base
from routes.router import router
app = FastAPI()

Base.metadata.create_all(bind = engine)

 
@app.get("/")
async def root():
    return {"message": "Hellooo 1111111!!!!"}

app.include_router(router,prefix="/users", tags=["user"])