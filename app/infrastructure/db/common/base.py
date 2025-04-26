from sqlalchemy.orm import sessionmaker, declarative_base
from .. import engine

Base = declarative_base()
SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine.engine
)