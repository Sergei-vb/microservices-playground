from core.db import session_local


async def get_session():
    async with session_local() as session:
        yield session
