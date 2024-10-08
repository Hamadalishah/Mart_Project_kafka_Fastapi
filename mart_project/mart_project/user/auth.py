from typing import Annotated
from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from mart_project.mart_project.user.db import get_session
from mart_project.user import Creat_User, User
from passlib.context import CryptContext #type: ignore
from aiokafka import AIOKafkaProducer #type: ignore
pwd_context = CryptContext(schemes=["bcrypt"])


async def password_verfy(palin_password, hash_password):
    return pwd_context.verify(palin_password,hash_password)

async def hash_password(password):
    return pwd_context.hash(password)

async def produce_message():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:19092')
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()
        
    



async def current_user(user:Annotated[Creat_User,Depends()],
                       session:Annotated[Session,Depends(get_session)]):
    existing_user = session.exec(
        select(User).where(User.userName == user.userName)).first()
    if  existing_user:
        raise HTTPException(status_code=404, detail="User already exists")
    existing_email = session.exec(
        select(User).where(User.email == user.email)).first()
    if existing_email:
        raise HTTPException(status_code=404, detail="Email already exists")
    return user

async def creat_user(user:Annotated[Creat_User,Depends(current_user)],
                     session:Annotated[Session,Depends(get_session)],
                     producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    hashed_password = await hash_password(user.password)
    user = User(userName=user.userName,email=user.email,password=hashed_password)
    session.add(user)  
    session.commit()
    session.refresh(user)
      