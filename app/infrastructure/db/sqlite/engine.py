from sqlalchemy import create_engine
from app.core.config import config

DATABASE_URL = config.get_database_url()

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}
)