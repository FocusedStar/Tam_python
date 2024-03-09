from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field, EmailStr


class User_schema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        from_attributes = True
        the_schema = {
            'user_demo': {
                "name": "Saif",
                "email": "Saif@example.com",
                "password": "123"
            }
        }

class UserLogin_schema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        from_attributes = True
        the_schema = {
            'user_demo': {
                "email": "Saif@example.com",
                "password": "123"
            }
        }        
class RequestUser(BaseModel):
    parameter: User_schema = Field(...)



