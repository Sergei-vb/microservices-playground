import uvicorn

from core import settings
from core.metrics import METRICS_INFO


if __name__ == '__main__':
    METRICS_INFO.info({"version": "1", "config": "develop"})
    uvicorn.run(
        'core.application:app',
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_RELOAD,
        debug=settings.SERVER_DEBUG,
        access_log=settings.SERVER_ACCESS_LOG,
        log_level=settings.SERVER_LOG_LEVEL,
    )
