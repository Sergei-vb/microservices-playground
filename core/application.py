import time

from fastapi import FastAPI, Request

from api.router import api_router
from core.metrics import METRICS_REQUEST_COUNT, METRICS_REQUEST_LATENCY
from core.router import router as core_router


def _create_app() -> FastAPI:
    app_ = FastAPI(title='microservices-playground')
    app_.include_router(core_router)
    app_.include_router(api_router, prefix='/api', tags=['api'])

    @app_.middleware('http')
    async def add_metrics(request: Request, call_next):
        prometheus_metrics_request_start_time = time.time()
        response = await call_next(request)
        request_latency = time.time() - prometheus_metrics_request_start_time

        METRICS_REQUEST_LATENCY.labels(request.method, request.url.path).observe(
            request_latency
        )
        METRICS_REQUEST_COUNT.labels(
            request.method, request.url.path, response.status_code
        ).inc()

        return response

    return app_


app = _create_app()
