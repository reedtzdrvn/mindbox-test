from app.infrastructure.db.repositories import SQLProductRepository
from app.services.product_service import ProductService


def get_product_service() -> ProductService:
    repo = SQLProductRepository()
    service = ProductService(repo)

    return service