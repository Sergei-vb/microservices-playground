import os

from fastapi import APIRouter


router = APIRouter()


@router.get('/health/')
async def get_health():
    return {'status': 'OK'}


@router.get('/')
async def get_root():
    return 'Hello world from ' + os.environ['HOSTNAME'] + ' !'
