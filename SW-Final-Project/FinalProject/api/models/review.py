from sqlalchemy import Column, Integer, String, ForeignKey, Text
from api.dependencies.database import Base

class Review(Base):
    __tablename__ = "review"

    reviewID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reviewText = Column(Text, nullable=False)
    reviewRating = Column(Integer, nullable=False)

    customerID = Column(Integer, ForeignKey("customer.customerID"), nullable=False)
    sandwichID = Column(Integer, ForeignKey("sandwiches.sandwichID"), nullable=False)