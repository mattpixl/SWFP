from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import resource as controller
from ..schemas import resource as schema
from ..dependencies.database import get_db

router = APIRouter(tags=["Resource"], prefix="/resources")

@router.post("/", response_model=schema.Resource)
def create(request: schema.ResourceCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.Resource])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Resource)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.Resource)
def update(item_id: int, request: schema.ResourceUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)

@router.get("/low-stock/{minimum_amount}", response_model=list[schema.Resource])
def low_stock(minimum_amount: float, db: Session = Depends(get_db)):
    return controller.low_stock(db, minimum_amount)