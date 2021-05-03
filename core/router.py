import os

from fastapi import APIRouter


router = APIRouter()


@router.get('/health/')
async def get_health():
    return {'status': 'OK'}


@router.get('/')
async def get_root():
    return (
        os.environ.get('GREETING', 'Hello world')
        + ' from ' + os.environ['HOSTNAME'] + ' !'
    )
