from copy import deepcopy

from fastapi import APIRouter, Path, Depends, Body, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from api import crud
from api.dependencies import get_session
from api.schemas.users import UserSchema
from core.models import User
from core.settings import JSON_CONTENT_TYPE


router = APIRouter()


@router.post(
    '/',
    response_model=UserSchema,
    response_class=JSONResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    session: AsyncSession = Depends(get_session),
    schema: UserSchema = Body(..., media_type=JSON_CONTENT_TYPE),
) -> JSONResponse:
    content: dict = schema.dict()
    content.pop('id')
    result_id = await crud.create(session, User, content)
    content.update({'id': result_id})
    return JSONResponse(content, status_code=status.HTTP_201_CREATED)


@router.get(
    '/{id}',
    response_model=UserSchema,
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
)
async def read_by_id(
    session: AsyncSession = Depends(get_session),
    user_id: int = Path(..., alias='id', ge=1),
) -> JSONResponse:
    result = await crud.read(session, User, user_id)

    if not result:
        raise HTTPException(status_code=404, detail='User is not found!')

    content = UserSchema.to_dict(result)
    return JSONResponse(content, status_code=status.HTTP_200_OK)


@router.put(
    '/{id}',
    response_model=UserSchema,
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
)
async def update_full_by_id(
    session: AsyncSession = Depends(get_session),
    user_id: int = Path(..., alias='id', ge=1),
    schema: UserSchema = Body(..., media_type=JSON_CONTENT_TYPE),

) -> JSONResponse:
    content: dict = schema.dict()
    data_to_update = deepcopy(content)
    data_to_update.pop('id')
    await crud.update(session, User, user_id, data_to_update)
    content.update({'id': user_id})
    return JSONResponse(content, status_code=status.HTTP_200_OK)


@router.delete(
    '/{id}',
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
)
async def delete_by_id(
    session: AsyncSession = Depends(get_session),
    user_id: int = Path(..., alias='id', ge=1),
) -> JSONResponse:
    await crud.delete(session, User, user_id)
    return JSONResponse({}, status_code=status.HTTP_200_OK)
