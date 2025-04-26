from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.infrastructure.db.common.base import Base
from app.infrastructure.db import engine

from app.api.routes.product import router as products_router
from app.core.init_db import seed_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_db()
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title='Mindbox Test API',
        lifespan=lifespan
    )

    app.include_router(
        products_router,
        prefix='/products',
        tags=['Products']
    )

    return app


app = create_app()