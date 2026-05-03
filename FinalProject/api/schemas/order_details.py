from typing import Optional
from pydantic import BaseModel, ConfigDict

class OrderDetailBase(BaseModel):
    order_id: int
    sandwich_id: int
    amount: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int

    model_config = ConfigDict(from_attributes=True)