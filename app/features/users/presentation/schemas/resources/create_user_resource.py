from pydantic import BaseModel

class CreateUserResource(BaseModel):
    name: str
    email: str
    password: str