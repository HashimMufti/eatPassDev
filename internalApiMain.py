import eatPassDev
import gruntFunctions
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    response = gruntFunctions.validate(eatPassDev.findGoogleLocation())
    print(response)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
