from fastapi import FastAPI

from api.router import api_router
from core.router import router as core_router


def _create_app() -> FastAPI:
    app_ = FastAPI(title='microservices-playground')
    app_.include_router(core_router)
    app_.include_router(api_router)

    return app_


app = _create_app()
