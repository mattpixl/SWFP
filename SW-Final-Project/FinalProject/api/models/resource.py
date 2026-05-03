from sqlalchemy import Column, String, Float
from api.dependencies.database import Base

class Resource(Base):
    __tablename__ = "resource"

    resourceIngredient = Column(String(30), primary_key=True, index=True)
    resourceAmount = Column(Float, nullable=False)
    resourceUnit = Column(String(15), nullable=False)