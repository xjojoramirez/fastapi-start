from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.item import Item as ItemModel
from app.schemas.item import ItemCreate, Item

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=Item)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    db_item = ItemModel(**item.dict(), owner_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return (
        db.query(ItemModel)
        .filter(ItemModel.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
        .all()
    )

@router.get("/{item_id}", response_model=Item)
def read_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not item or item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=Item)
def update_item(
    item_id: int,
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item or db_item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    for field, value in item.dict().items():
        setattr(db_item, field, value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item or db_item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}
