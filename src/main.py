from fastapi import FastAPI

from models.models import Name, Status

import random

app = FastAPI()

@app.get('/items',response_model=list[Name])
async def items():
    items = [{"name":"item1"},{"name":"item2"}]
    return items

@app.post('/add/',response_model=Status)
async def add(name: Name):
    num = random.randint(1,3)
    if num == 1:
        items = {"status":"error"}
    else:
        items = {"status": "ok"}
    return items

@app.delete('/items',response_model=Status)
async def add(name: Name):
    items = {"status": "ok"}
    return items


