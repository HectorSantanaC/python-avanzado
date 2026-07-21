from fastapi import FastAPI
from api.v1.api import api_router

app = FastAPI(
  title="E-commerce API",
  description="""
    Api RESTfull completa para la gestión de un E-commerce

    Incluye:
    - Autenticación con JWT
    - Administración de productos y categorías
    - Carrito de compras
    - Gestión de pedidos
  """,
  version="1.0.0",
  contact={
    "name": "Héctor Dev - Equipo Backend",
    "url": "http://github.com/",
    "email": "contacto@email.com"
  },
  license_info={
    "name": "MIT License",
    "url": "https://opensource.org/licences/MIT"
  }
)

app.include_router(api_router, prefix="/api/v1")