from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret


config = Config()

SERVER_HOST = config('SERVER_HOST', cast=str, default='0.0.0.0')
SERVER_PORT = config('SERVER_PORT', cast=int, default=80)


DEBUG = config('DEBUG', cast=bool, default=False)
ACCESS_LOG = config('ACCESS_LOG', cast=bool, default=False)
RELOAD = config('RELOAD', cast=bool, default=False)
LOG_LEVEL = 'debug' if DEBUG else config('LOG_LEVEL', cast=str, default='info').lower()


DATABASE = {
    'DB_DRIVER_ASYNC': config('DB_DRIVER_ASYNC', default='postgresql+asyncpg'),
    'DB_DRIVER_SYNC': config('DB_DRIVER_SYNC', default='postgresql'),
    'NAME': config('DB_NAME'),
    'USER': config('DB_USER'),
    'PASSWORD': config('DB_PASSWORD', cast=Secret),
    'HOST': config('DB_HOST'),
    'PORT': config('DB_PORT'),
}
DB_DSN = config(
    'DB_DSN',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_ASYNC'],
        username=DATABASE['USER'],
        password=DATABASE['PASSWORD'],
        host=DATABASE['HOST'],
        port=DATABASE['PORT'],
        database=DATABASE['NAME'],
    ),
)
DB_DSN_ALEMBIC = config(
    'DB_DSN_ALEMBIC',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_SYNC'],
        username=DATABASE['USER'],
        password=DATABASE['PASSWORD'],
        host=DATABASE['HOST'],
        port=DATABASE['PORT'],
        database=DATABASE['NAME'],
    ),
)

JSON_CONTENT_TYPE = 'application/json'
