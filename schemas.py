# skema data

from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str 
    description: str 

class ItemCreate(ItemBase):
    pass

class ItemRespnse(ItemBase):
    id: int 

    class Config:
        orm_mode = True