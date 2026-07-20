from sqlalchemy import Column, Integer, String, Datetime, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class carrito(Base):
  __tablename__ = "carritos"
  id = Column(Integer, primary_key=True, index=True)
  usuario_id = Column(Integer, ForeignKey("usuarios.id"))
  usuario = relationship("Usuario", back_populates="carrito")
  items = relationship("ItemCarrito", back_populates="carrito", cascade="all, delete")

class ItemCarrito(Base):
  __tablename__ = "items_carrito"
  id = Column(Integer, primary_key=True, index=True)
  carrito_id = Column(Integer, ForeignKey("carrito.id"))
  producto_id = Column(Integer, ForeignKey("productos.id"))
  cantidad = Column(Integer, default=1)
  carrito = relationship("Carrito", back_populates="items")
  producto = relationship("Producto")


class Pedido(Base):
  id = Column(Integer, primary_key=True, index=True)
  fecha = Column(Datetime, default=datetime.now.utcnow)
  total = Column(Float)
  detalles = relationship("DetallePedido", back_populates="pedido")