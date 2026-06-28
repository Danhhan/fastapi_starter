from pydantic import BaseModel


class CreateUserPayload(BaseModel):
    email: str
    full_name: str
    password: str
