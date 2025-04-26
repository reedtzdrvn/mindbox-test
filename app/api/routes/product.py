from typing import List, Tuple
from fastapi import APIRouter, Depends

from app.api.dependencies import get_product_service
from app.domain.schemas import ProductResponse, CategoryResponse, ProductCategoryPairsResponse
from app.services.product_service import ProductService


router = APIRouter()

@router.get('/', response_model=List[ProductResponse], tags=['Products'])
async def list_products(service: ProductService = Depends(get_product_service)):
    return service.list_products_with_categories()

@router.get('/categories', response_model=List[CategoryResponse], tags=['Products'])
async def list_categories(service: ProductService = Depends(get_product_service)):
    return service.list_categories()

@router.get('/pairs', response_model=List[ProductCategoryPairsResponse], tags=['Products'])
async def list_pairs(service: ProductService = Depends(get_product_service)):
    return service.list_product_category_pairs()