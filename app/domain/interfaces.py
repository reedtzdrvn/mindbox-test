from abc import ABC, abstractmethod
from typing import List, Tuple

from .models import Category, Product


class IProductRepository(ABC):
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod 
    def get_all_categories(self) -> List[Category]:
        pass

    @abstractmethod
    def get_product_category_pairs(self) -> List[Tuple[str, str]]:
        pass