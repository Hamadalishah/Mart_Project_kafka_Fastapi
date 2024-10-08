from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class User(SQLModel):
    id: int = Field(default=None)
    userName: str = Field(index=True)
    email: str = Field(index=True)
    password: str
    
class Creat_User(BaseModel):
    userName: str 
    email: str 
    password: str
    
    

    