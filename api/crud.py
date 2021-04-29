from sqlalchemy import insert, select
from sqlalchemy import delete as delete_stmt
from sqlalchemy import update as update_stmt
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import Base


async def create(
    session: AsyncSession,
    entity: Base,
    data: dict,
) -> int:  # TODO: check
    stmt_create = insert(entity).values(**data).returning(entity.id)
    result = await session.execute(stmt_create)
    await session.commit()
    return result.scalars().first()


async def read(
    session: AsyncSession,
    entity: Base,
    entry_id: int,
) -> Base:
    stmt = select(entity).filter(entity.id == entry_id)
    result = await session.execute(stmt)
    return result.scalars().first()


async def update(
    session: AsyncSession,
    entity: Base,
    entry_id: int,
    data: dict,
) -> None:
    stmt = update_stmt(entity).where(entity.id == entry_id).values(**data)
    await session.execute(stmt)
    await session.commit()


async def delete(
    session: AsyncSession,
    entity: Base,
    entry_id: int,
) -> None:
    stmt = delete_stmt(entity).where(entity.id == entry_id)
    await session.execute(stmt)
    await session.commit()
