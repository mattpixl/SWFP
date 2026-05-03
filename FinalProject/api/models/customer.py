from sqlalchemy import Column, Integer, String
from api.dependencies.database import Base

class Customer(Base):
    __tablename__ = "customer"

    customerID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customerName = Column(String(100), nullable=False)
    customerEmail = Column(String(100), nullable=False)
    customerPhone = Column(String(20), nullable=False)
    customerAddress = Column(String(255), nullable=False)