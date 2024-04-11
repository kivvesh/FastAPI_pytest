import random

from fastapi import FastAPI

from models.models import Name, Status
from api.v1 import items
from tests.functional.settings import test_settings


app = FastAPI(
    title = test_settings.title_app,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json'
)

app.include_router(items.router)
