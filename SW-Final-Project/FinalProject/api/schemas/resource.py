from typing import Optional
from pydantic import BaseModel, ConfigDict


class ResourceBase(BaseModel):
    resourceIngredient: str
    resourceAmount: float
    resourceUnit: str


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    resourceIngredient: Optional[str] = None
    resourceAmount: Optional[float] = None
    resourceUnit: Optional[str] = None


class Resource(ResourceBase):
    model_config = ConfigDict(from_attributes=True)