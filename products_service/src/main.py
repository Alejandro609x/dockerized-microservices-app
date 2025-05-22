# Importa FastAPI para crear la aplicación web
from fastapi import FastAPI
# Importa el router definido en products_controller para manejar rutas de productos
from src.controllers.products_controller import router as products_router

# Crea la instancia principal de la aplicación FastAPI con título personalizado
app = FastAPI(title="Products Service")

# Añade las rutas del router de productos bajo el prefijo "/products"
app.include_router(products_router, prefix="/products")
