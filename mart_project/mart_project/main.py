from fastapi import FastAPI
from aiokafka import AIOKafkaProducer  # type: ignore
from sqlmodel import Field, SQLModel
import json
app = FastAPI()




class Product(SQLModel):
    id:int |  None = Field(default=None)
    name: str = Field(index=True)
    price: float = Field(default=False)
    quantity: int
    category: str




@app.post('/product')

async def get_product(product:Product):
    
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    product_json  = json.dumps(product.__dict__).encode("utf-8")
    
    await producer.start()
    try:

        await producer.send_and_wait('product', product_json)
    finally:
        
        await producer.stop()
    return product_json



@app.get("/")
async def root():
    return {"message": "Welcome to the Mart API"}
