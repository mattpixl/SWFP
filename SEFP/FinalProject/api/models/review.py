from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class Review(Base):
    __tablename__ = "review"

    reviewID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reviewText = Column(Text, nullable=False)
    reviewRating = Column(Integer, nullable=False)

    customerID = Column(Integer, ForeignKey("customer.customerID"), nullable=False)
    sandwichID = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)

    sandwich = relationship("Sandwich", back_populates="reviews")