from typing import Optional
from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    customerName: str
    customerEmail: str
    customerPhone: str
    customerAddress: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    customerName: Optional[str] = None
    customerEmail: Optional[str] = None
    customerPhone: Optional[str] = None
    customerAddress: Optional[str] = None


class Customer(CustomerBase):
    customerID: int

    model_config = ConfigDict(from_attributes=True)