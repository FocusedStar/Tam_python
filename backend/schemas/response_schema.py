from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class Response (BaseModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T]= None