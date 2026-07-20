from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import carrito as crud_carrito
from deps.deps import get_db, get_current_user

router = APIRouter()

@router.get("/", summary="Ver contenido del carrito")
def ver_carrito(db: Session = Depends(get_db), user = Depends(get_current_user)):
  carrito = crud_carrito.obterner_carrito(db, user.id)
  return carrito