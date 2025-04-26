from sqlalchemy.orm import selectinload

from app.infrastructure.db.common.models import CategoryModel, ProductModel
from app.infrastructure.db.common.base import SessionLocal
from app.domain.interfaces import IProductRepository
from app.domain.models import Category, Product

class SQLProductRepository(IProductRepository):
    def __init__(self):
        self._Session = SessionLocal

    def get_all_products(self):
        with self._Session() as db:
            products = db.query(ProductModel).options(selectinload(ProductModel.categories)).all()

            return [
                Product(
                    id=p.id,
                    name=p.name,
                    categories=[
                        Category(
                            id=c.id,
                            name=c.name,
                            products=[]
                        ) for c in p.categories
                    ]
                )
                for p in products
            ]
        
    def get_all_categories(self):
        with self._Session() as db:
            db_categories = (
                db.query(CategoryModel)
                .options(selectinload(CategoryModel.products))
                .all()
            )
            return [
                Category(
                    id=c.id,
                    name=c.name,
                    products=[
                        Product(
                            id=p.id,
                            name=p.name,
                            categories=[]
                        ) for p in c.products
                    ]
                )
                for c in db_categories
            ]
            
    def get_product_category_pairs(self):
        with self._Session() as db:
            rows = (
                db.query(ProductModel.name, CategoryModel.name)
                    .join(ProductModel.categories)
                    .all()
            )

            return [(prod, cat) for prod, cat in rows]