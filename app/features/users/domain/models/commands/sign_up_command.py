from pydantic import BaseModel

class SignUpCommand(BaseModel):
    name: str
    email: str
    plain_password: str