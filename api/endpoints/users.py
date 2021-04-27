from fastapi import APIRouter, Path

from api import crud


router = APIRouter()


@router.post('/')
async def create():
    return


@router.get('/{id}')
async def read_by_id(user_id: int = Path(..., alias='id', ge=1)):
    return


@router.put('/{id}')
async def update_full_by_id(user_id: int = Path(..., alias='id', ge=1)):
    return


@router.delete('/{id}')
async def delete_by_id(user_id: int = Path(..., alias='id', ge=1)):
    return
