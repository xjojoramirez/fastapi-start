from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import engine, get_db, Base
from app.schemas import ItemCreate, ItemUpdate, ItemResponse
import app.crud as crud
import app.models  # noqa: F401 — ensures models are registered

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD", version="1.0.0")


@app.get("/")
def root():
    return {"message": "FastAPI CRUD is running ��"}


# ─── CREATE ───────────────────────────────────────────────────
@app.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


# ─── READ ALL ─────────────────────────────────────────────────
@app.get("/items/", response_model=List[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return crud.get_all_items(db)


# ─── READ ONE ─────────────────────────────────────────────────
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# ─── UPDATE ───────────────────────────────────────────────────
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


# ─── DELETE ───────────────────────────────────────────────────
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
