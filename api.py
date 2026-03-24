from fastapi import FastAPI
from database import get_user

app = FastAPI()

@app.get("/user/{id}")
def user(id:int):
    return {"data": get_user(id)}
