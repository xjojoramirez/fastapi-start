from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate, ItemUpdate


def get_all_items(db: Session):
    return db.query(Item).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: ItemCreate):
    new_item = Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def update_item(db: Session, item_id: int, item: ItemUpdate):
    db_item = get_item_by_id(db, item_id)
    if not db_item:
        return None
    # Only update fields that were actually sent
    for field, value in item.model_dump(exclude_unset=True).items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    db_item = get_item_by_id(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
