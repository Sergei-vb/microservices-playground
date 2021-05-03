from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config


config = Config()

SERVER_HOST = config('SERVER_HOST', cast=str, default='0.0.0.0')
SERVER_PORT = config('SERVER_PORT', cast=int, default=80)


SERVER_DEBUG = config('SERVER_DEBUG', cast=bool, default=False)
SERVER_ACCESS_LOG = config('SERVER_ACCESS_LOG', cast=bool, default=False)
SERVER_RELOAD = config('SERVER_RELOAD', cast=bool, default=False)
SERVER_LOG_LEVEL = (
    'debug'
    if SERVER_DEBUG
    else config('SERVER_LOG_LEVEL', cast=str, default='info').lower()
)


DATABASE = {
    'DB_DRIVER_ASYNC': config('DB_DRIVER_ASYNC', default='postgresql+asyncpg'),
    'DB_DRIVER_SYNC': config('DB_DRIVER_SYNC', default='postgresql'),
    'DB_NAME': config('DB_NAME'),
    'DB_USER': config('DB_USER'),
    'DB_PASSWORD': config('DB_PASSWORD'),
    'DB_HOST': config('DB_HOST'),
    'DB_PORT': config('DB_PORT'),
}
DB_DSN = config(
    'DB_DSN',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_ASYNC'],
        username=DATABASE['DB_USER'],
        password=DATABASE['DB_PASSWORD'],
        host=DATABASE['DB_HOST'],
        port=DATABASE['DB_PORT'],
        database=DATABASE['DB_NAME'],
    ),
)
DB_DSN_ALEMBIC = config(
    'DB_DSN_ALEMBIC',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_SYNC'],
        username=DATABASE['DB_USER'],
        password=DATABASE['DB_PASSWORD'],
        host=DATABASE['DB_HOST'],
        port=DATABASE['DB_PORT'],
        database=DATABASE['DB_NAME'],
    ),
)

JSON_CONTENT_TYPE = 'application/json'
