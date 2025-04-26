from app.core.config import POSTGRESQL, SQLITE, config

if config.DB_TYPE == POSTGRESQL:
    from .postgres.engine import engine
elif config.DB_TYPE == SQLITE:
    from .sqlite.engine import engine
else:
    raise ValueError('Unsupported DB_TYPE: ' + config.DB_TYPE)