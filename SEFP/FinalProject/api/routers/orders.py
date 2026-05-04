from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Orders"],
    prefix="/orders"
)

@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Order)
def update(
    item_id: int,
    request: schema.OrderUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

@router.get("/tracking/{tracking_number}", response_model=schema.Order)
def get_by_tracking_number(tracking_number: int, db: Session = Depends(get_db)):
    return controller.get_by_tracking_number(db, tracking_number)

@router.get("/date/{order_date}", response_model=list[schema.Order])
def get_orders_by_date(order_date: date, db: Session = Depends(get_db)):
    return controller.get_orders_by_date(db, order_date)

@router.get("/date-range/{start_date}/{end_date}", response_model=list[schema.Order])
def get_orders_by_date_range(start_date: date, end_date: date, db: Session = Depends(get_db)):
    return controller.get_orders_by_date_range(db, start_date, end_date)

@router.get("/revenue/{order_date}")
def get_revenue_by_date(order_date: date, db: Session = Depends(get_db)):
    return controller.get_revenue_by_date(db, order_date)

@router.put("/{item_id}/pay", response_model=schema.Order)
def pay_order(item_id: int, db: Session = Depends(get_db)):
    return controller.pay_order(db, item_id)
