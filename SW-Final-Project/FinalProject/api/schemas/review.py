from typing import Optional
from pydantic import BaseModel, ConfigDict


class ReviewBase(BaseModel):
    reviewText: str
    reviewScore: int
    customerID: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    reviewText: Optional[str] = None
    reviewScore: Optional[int] = None
    customerID: Optional[int] = None


class Review(ReviewBase):
    reviewID: int

    model_config = ConfigDict(from_attributes=True)