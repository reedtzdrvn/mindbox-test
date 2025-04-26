from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class Category:
    id: int
    name: str
    products: List[Product]

@dataclass
class Product:
    id: int
    name: str
    categories: List[Category]