from typing import List, Tuple
from app.domain.models import Category, Product
from app.domain.schemas import ProductResponse, CategoryResponse, ProductBasic, CategoryBasic, ProductCategoryPairsResponse
from app.domain.interfaces import IProductRepository


class ProductService:
    def __init__(self, repo: IProductRepository):
        self.repo = repo

    def list_products_with_categories(self) -> List[ProductResponse]:
        products = self.repo.get_all_products()
        return [
            ProductResponse(
                id=product.id,
                name=product.name,
                categories=[
                    CategoryBasic(id=category.id, name=category.name)
                    for category in product.categories
                ]
            )
            for product in products
        ]
    
    def list_categories(self) -> List[CategoryResponse]:
        categories = self.repo.get_all_categories()
        return [
            CategoryResponse(
                id=category.id,
                name=category.name,
                products=[
                    ProductBasic(id=product.id, name=product.name)
                    for product in category.products
                ]
            )
            for category in categories
        ]
    
    def list_product_category_pairs(self) -> List[Tuple[str, str]]:
        product_pairs = self.repo.get_product_category_pairs()
        return [
            ProductCategoryPairsResponse(
                product=product_name,
                category=category_name
            )
            for product_name, category_name in product_pairs
        ]
