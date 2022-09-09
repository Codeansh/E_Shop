from pydantic import BaseModel
from typing import Optional


# For validation
class Product(BaseModel):
    name: str
    price: int
    count: int = 0
    in_stack: bool = False
    rating: Optional[int] = 0



