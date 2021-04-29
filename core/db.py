from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from core import settings


Base = declarative_base()


def get_engine() -> AsyncEngine:
    return create_async_engine(settings.DB_DSN, echo=True, poolclass=NullPool)


session_local = sessionmaker(
    bind=get_engine(), expire_on_commit=False, class_=AsyncSession
)
