import random

from fastapi import APIRouter

from src.models.models import Name, Status

router = APIRouter()
@router.get('/items',response_model=list[Name])
async def items():
    '''
    GET-method /items
    '''
    items = [{"name":"item1"},{"name":"item2"}]
    return items

@router.post('/add',response_model=Status)
async def add(name: Name):
    '''
        POST-method /add
    '''
    num = random.randint(1,3)
    if num == 1:
        items = {"status":"error"}
    else:
        items = {"status": "ok"}
    return items

@router.delete('/items',response_model=Status)
async def add(name: Name):
    '''
        DELETE-method /items
    '''
    items = {"status": "ok"}
    return items
