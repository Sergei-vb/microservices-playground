from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int = None
    username: str
    first_name: str = None
    last_name: str = None
    email: str
    phone: str = None

    class Config:
        orm_mode = True
