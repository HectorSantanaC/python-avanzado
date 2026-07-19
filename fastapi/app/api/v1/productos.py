from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from deps.deps import get_db, require_admin
from crud.producto import obtener_productos, crear_producto
from schemas.producto import ProductoResponse, ProductoCreate

api_router = APIRouter()

@api_router.get("/productos", response_model=list[ProductoResponse])
def listar_productos(db:Session = Depends(get_db)):
  return obtener_productos(db)

@api_router.post("/productos", response_model=ProductoCreate, dependencies=[Depends(require_admin)])
def agregar_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
  return crear_producto(db, producto)

@api_router.put("/productos/{id}", response_model=list[ProductoResponse])
def actualizar_producto(producto_id: int, datos: ProductoCreate, db: Session = Depends(get_db)):
  producto = actualizar_producto(db, producto_id, datos)

  if not producto:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  
  return producto

@api_router.delete("/productos/{id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
  producto = eliminar_producto(db, producto_id)

  if not producto:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  return {"mensaje": "Producto eliminado"}