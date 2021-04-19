from fastapi import FastAPI

from .router import router


def _create_app() -> FastAPI:
    app_ = FastAPI(title='microservices-playground')
    app_.include_router(router)
    return app_


app = _create_app()


@app.get('/health/')
async def get_health():
    return {'status': 'OK'}
