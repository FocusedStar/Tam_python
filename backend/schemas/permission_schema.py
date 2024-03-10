from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field, EmailStr



class Permission_schema(BaseModel):
    id: Optional[int]=None
    permission: str=None
    class Config:
        from_attributes = True
        the_schema = {
            'user_demo': {
                "id": "0",
                "permission": "admin"
            }
        }  

class RequestPermission(BaseModel):
    parameter: Permission_schema = Field(...)