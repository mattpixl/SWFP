from sqlalchemy.orm import Session
from ..models import promotion as model
from .crud_factory import create_item, read_all_items, read_one_item, update_item, delete_item

def create(db: Session, request):
    return create_item(db, model.Promotion, request)

def read_all(db: Session):
    return read_all_items(db, model.Promotion)

def read_one(db: Session, item_id: str):
    return read_one_item(db, model.Promotion, model.Promotion.promotionCode, item_id)

def update(db: Session, item_id: str, request):
    return update_item(db, model.Promotion, model.Promotion.promotionCode, item_id, request)

def delete(db: Session, item_id: str):
    return delete_item(db, model.Promotion, model.Promotion.promotionCode, item_id)