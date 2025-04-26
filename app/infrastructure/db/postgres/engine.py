from app.core.config import config
from sqlalchemy import create_engine

DATABASE_URL = config.get_database_url()

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20
)