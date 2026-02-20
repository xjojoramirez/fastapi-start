from fastapi import APIRouter, Depends
from app.api.deps import get_current_user

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
def read_items(current_user = Depends(get_current_user)):
    return {"message": f"Hello {current_user.email}"}
