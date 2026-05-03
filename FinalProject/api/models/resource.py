from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resourceIngredient = Column(String(30), unique=True, nullable=False)
    resourceAmount = Column(Float, nullable=False)
    resourceUnit = Column(String(15), nullable=False)

    recipes = relationship("Recipe", back_populates="resource")