import uvicorn

from core import settings


if __name__ == '__main__':
    uvicorn.run(
        'core.application:app',
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.RELOAD,
    )
