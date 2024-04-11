import random

from fastapi import FastAPI

from src.models.models import Name, Status
from src.api.v1 import items
from src.tests.functional.settings import test_settings


app = FastAPI(
    title = test_settings.title_app,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json'
)

app.include_router(items.router)
