from sqlalchemy import Column, String, Date
from api.dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotion"

    promotionCode = Column(String(10), primary_key=True, index=True)
    promotionExpire = Column(Date, nullable=False)