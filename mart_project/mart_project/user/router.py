from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session

from mart_project.mart_project.user.auth import current_user
from mart_project.mart_project.user.db import get_session
from mart_project.mart_project.user.schema import User



router = APIRouter(   
    prefix= "/user",
    tags= ["User Microservices"],
    responses= {404: {"description":"not found"}})

@router.post("/register/")
async def create_user(user:Annotated[User,Depends(current_user)],session:Annotated[Session,Depends(get_session)]):
  
    return user