import os

from fastapi import FastAPI
import uvicorn


app = FastAPI(title='microservices-playground')


@app.get('/health/')
async def get_health():
    return {'status': 'OK'}


@app.get('/')
async def get_root():
    return 'Hello world from ' + os.environ['HOSTNAME'] + ' !'


if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=80, reload=False)
