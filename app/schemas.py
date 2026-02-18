from pydantic import BaseModel
from typing import Optional


# Used when CREATING an item (no id yet)
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# Used when UPDATING an item (all fields optional)
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


# Used in RESPONSES (includes id)
class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        from_attributes = True
