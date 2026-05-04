from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict

class OrderBase(BaseModel):
    orderDate: date
    trackingNumber: int
    orderStatus: str
    orderPrice: float
    orderCustomerID: Optional[int] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    orderDate: Optional[date] = None
    trackingNumber: Optional[int] = None
    orderStatus: Optional[str] = None
    orderPrice: Optional[float] = None
    orderCustomerID: Optional[int] = None
    orderType: Optional[str] = None
    paymentStatus: Optional[str] = None
    promotionCode: Optional[str] = None

class Order(OrderBase):
    orderID: int

    model_config = ConfigDict(from_attributes=True)
    orderType: str = "takeout"
    paymentStatus: str = "unpaid"
    promotionCode: Optional[str] = None