from typing import List
from pydantic import BaseModel


class CategoryBasic(BaseModel):
    id: int
    name: str


class ProductBasic(BaseModel):
    id: int
    name: str


class ProductResponse(BaseModel):
    id: int
    name: str
    categories: List[CategoryBasic]


class CategoryResponse(BaseModel):
    id: int
    name: str
    products: List[ProductBasic]


class ProductCategoryPairsResponse(BaseModel):
    product: str
    category: str