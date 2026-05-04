from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PromotionBase(BaseModel):
    promotionCode: str
    promotionExpire: date


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promotionCode: Optional[str] = None
    promotionExpire: Optional[date] = None


class Promotion(PromotionBase):
    model_config = ConfigDict(from_attributes=True)