from sqlalchemy import Column, Integer, String, Text, Float
from api.dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    menuID = Column(Integer, primary_key=True, index=True)
    menuDish = Column(String(50), nullable=False)
    menuIngredients = Column(Text, nullable=False)
    menuPrice = Column(Float, nullable=False)
    menuCalories = Column(Integer, nullable=False)
    menuCategory = Column(String(30), nullable=False)