# skema data

from pydantic import BaseModel
from typing import List, Optional

# categories
class CategoryBase(BaseModel):
    name: str 
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int 
    items: List["ItemResponse"] = [] # Relasi ke items

    class Config:
        from_attributes = True


# items
class ItemBase(BaseModel):
    name: str 
    description: str
    #quantity: int 

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int 

    class Config:
        from_attributes = True



