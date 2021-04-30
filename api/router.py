from fastapi import APIRouter

from api.endpoints import users


api_router = APIRouter()


api_router.include_router(users.router, prefix='/user', tags=['user'])
