from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field


class User_schema(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    job: Optional[str]=None
    email: Optional[str]=None

    class Config:
        from_attributes = True

class RequestUser(BaseModel):
    parameter: User_schema = Field(...)

