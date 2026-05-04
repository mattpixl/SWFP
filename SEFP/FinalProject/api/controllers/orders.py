from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

from ..models import orders as model

def create(db: Session, request):
    new_item = model.Order(
        orderDate=request.orderDate,
        trackingNumber=request.trackingNumber,
        orderStatus=request.orderStatus,
        orderPrice=request.orderPrice,
        orderCustomerID=request.orderCustomerID
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return result


def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.Order).filter(
            model.Order.orderID == item_id
        ).first()

        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Id not found!"
            )

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return item


def update(db: Session, item_id: int, request):
    try:
        item = db.query(model.Order).filter(
            model.Order.orderID == item_id
        )

        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Id not found!"
            )

        update_data = request.model_dump(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return item.first()


def delete(db: Session, item_id: int):
    try:
        item = db.query(model.Order).filter(
            model.Order.orderID == item_id
        )

        if not item.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Id not found!"
            )

        item.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_by_tracking_number(db: Session, tracking_number: int):
    item = db.query(model.Order).filter(
        model.Order.trackingNumber == tracking_number
    ).first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tracking number not found!"
        )

    return item


def get_orders_by_date(db: Session, order_date):
    return db.query(model.Order).filter(
        model.Order.orderDate == order_date
    ).all()


def get_orders_by_date_range(db: Session, start_date, end_date):
    return db.query(model.Order).filter(
        model.Order.orderDate >= start_date,
        model.Order.orderDate <= end_date
    ).all()


def get_revenue_by_date(db: Session, order_date):
    total = db.query(func.sum(model.Order.orderPrice)).filter(
        model.Order.orderDate == order_date
    ).scalar()

    return {
        "orderDate": order_date,
        "totalRevenue": total or 0
    }


def pay_order(db: Session, item_id: int):
    item = db.query(model.Order).filter(
        model.Order.orderID == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Id not found!"
        )

    item.paymentStatus = "Paid"
    db.commit()
    db.refresh(item)

    return item