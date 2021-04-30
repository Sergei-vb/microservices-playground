from pydantic import BaseModel

from core.models import User


class UserSchema(BaseModel):
    id: int = None
    username: str
    first_name: str = None
    last_name: str = None
    email: str
    phone: str = None

    class Config:
        orm_mode = True

    @staticmethod
    def to_dict(user: User) -> dict:
        return {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
        }
