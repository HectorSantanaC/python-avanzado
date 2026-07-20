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