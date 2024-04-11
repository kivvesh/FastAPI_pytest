from pydantic import Field
from pydantic_settings import BaseSettings

class TestSettings(BaseSettings):
    sevice_url: str = Field(
        default='http://127.0.0.1:8000/'
    )

test_settings = TestSettings()