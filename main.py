from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Models(str, Enum):
    alexa = "Alexa"
    siri = "Siri"
    alisa = "Alisa" 


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}


@app.get("/users/me")
async def read_item():
    return {"user_id" : "current user"}


@app.get("/models/{model_name}")
async def read_item(model_name: Models):
    if model_name is Models.alexa:
        return {"Model is": model_name, "dev": "Amazon"}
    if model_name is Models.siri:
        return {"Model is": model_name, "dev": "Apple"}
    return {"Model is": model_name, "dev": "Yandex"}


@app.get("/users/{user_id}")
async def read_item(user_id:str):
    return {"item_id" : user_id}

@app.post("/items/")
async def create_item(item: Item):
    return item