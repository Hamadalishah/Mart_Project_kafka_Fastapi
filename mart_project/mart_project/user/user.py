from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import Session
from aiokafka import AIOKafkaProducer # type: ignore
from aiokafka import AIOKafkaConsumer # type: ignore
from mart_project.mart_project.user import router
from mart_project.mart_project.user.auth import current_user 
from .schema import Creat_User, User
import uvicorn # type: ignore
import os
producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    print("lifespan event fire....")
    yield
    
app = FastAPI(lifespan=lifespan)


app.include_router(router=router)


@app.get("/user/")
async def read_users():
    return producer


@app.post("/token")
async def login():
    pass
@app.get("/user/{user_id}")
async def get_user(user_id,session:Annotated[Session,Depends()]):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return user

@app.patch("/user/{user_id}")
async def update_user(user_id,user:Creat_User,session:Annotated[Session,Depends()]):
    user_db = session.query(User).filter(User.id == user_id).first()

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_db.userName = user.userName
    user_db.email = user.email
    session.commit()
    await producer.send(KAFKA_TOPIC, value={"type": "user_updated", "user_id": user_id})
    
    return user_db

@app.delete("/user/{user_id}")
async def delete_user(user_id,session:Annotated[Session,Depends()]):
    user_db = session.query(User).filter(User.id == user_id).first()

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user_db)
    session.commit()
    await producer.send(KAFKA_TOPIC, value={"type": "user_deleted", "user_id": user_id})

    return {"message": "User deleted successfully"}




