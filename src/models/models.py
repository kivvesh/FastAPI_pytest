from pydantic import BaseModel
class Name(BaseModel):
    name: str
class Status(BaseModel):
    status: str
