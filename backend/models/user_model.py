import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from database.database import Base

metadata = Base.metadata
 
#user model   
class User(Base):
    __tablename__ = "Users"
    id = sq.Column(sq.Integer, primary_key=True, nullable=False,autoincrement=True)
    name = sq.Column(sq.String(50), unique=True, nullable=False)
    job = sq.Column(sq.String(50), nullable=True)
    email = sq.Column(sq.String(50), unique=True, nullable=False)
    def __repr__(self):
        return f"id: {self.id}, User name: {self.name}"