from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    orderID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    orderDate = Column(Date, nullable=False)
    trackingNumber = Column(Integer, unique=True, nullable=False)
    orderStatus = Column(String(15), nullable=False)
    orderPrice = Column(Float, nullable=False)

    orderCustomerID = Column(
        Integer,
        ForeignKey("customer.customerID"),
        nullable=True
    )

    order_details = relationship("OrderDetail", back_populates="order")
    orderType = Column(String(20), nullable=False, server_default="takeout")
    paymentStatus = Column(String(20), nullable=False, server_default="unpaid")
    promotionCode = Column(String(10), ForeignKey("promotion.promotionCode"), nullable=True)