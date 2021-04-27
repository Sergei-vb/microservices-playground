from sqlalchemy import Column, Integer, String

from core.db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=256), nullable=False, unique=True)
    first_name = Column(String(length=64), nullable=True)
    last_name = Column(String(length=64), nullable=True)
    email = Column(String(length=128), nullable=False, unique=True)
    phone = Column(String(length=64), nullable=True, unique=True)

    def __repr__(self):
        return f'User(id={self.id!r}, username={self.username!r})'
