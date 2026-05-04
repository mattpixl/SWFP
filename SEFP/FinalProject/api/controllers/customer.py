from sqlalchemy.orm import Session
from ..models import customer as model
from .crud_factory import create_item, read_all_items, read_one_item, update_item, delete_item

def create(db: Session, request):
    return create_item(db, model.Customer, request)

def read_all(db: Session):
    return read_all_items(db, model.Customer)

def read_one(db: Session, item_id: int):
    return read_one_item(db, model.Customer, model.Customer.customerID, item_id)

def update(db: Session, item_id: int, request):
    return update_item(db, model.Customer, model.Customer.customerID, item_id, request)

def delete(db: Session, item_id: int):
    return delete_item(db, model.Customer, model.Customer.customerID, item_id)