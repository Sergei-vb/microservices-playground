import os

from fastapi import APIRouter, Response
from prometheus_client import generate_latest


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


@router.get('/metrics')
async def get_metrics():
    return Response(generate_latest(), media_type='plain/text')
