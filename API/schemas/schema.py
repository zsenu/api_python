from pydantic import BaseModel, EmailStr, Field
from typing import List

ShopName = 'Bolt'

class User(BaseModel):
    id: int = Field(..., ge = 0, description = "non-negative, unique integer id of the user")
    name: str = Field(..., min_length = 1, description = "name of the user")
    email: EmailStr = Field(..., description = "e-mail address of the user")

class Item(BaseModel):
    item_id: int = Field(..., ge = 0, description = "non-negative, unique integer id of the item")
    name: str = Field(..., min_length = 1, description = "name of the item")
    brand: str = Field(..., min_length = 1, description = "brand of the item")
    price: float = Field(..., ge = 0, description = "non-negative decimal price of the item")
    quantity: int = Field(..., ge = 0, description = "non-negative integer quantity of the item")

class Basket(BaseModel):
    id: int = Field(..., ge = 0, description = "non-negative, unique integer id of the basket")
    user_id: int = Field(..., ge = 0, description = "non-negative integer id of the user who owns the basket")
    items: List[Item] = Field(default_factory = list, description = "list of items in the basket")