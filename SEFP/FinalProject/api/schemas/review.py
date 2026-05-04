from typing import Optional
from pydantic import BaseModel, ConfigDict

class ReviewBase(BaseModel):
    reviewText: str
    reviewRating: int
    customerID: int
    sandwichID: int

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    reviewText: Optional[str] = None
    reviewRating: Optional[int] = None
    customerID: Optional[int] = None
    sandwichID: Optional[int] = None

class Review(ReviewBase):
    reviewID: int

    model_config = ConfigDict(from_attributes=True)