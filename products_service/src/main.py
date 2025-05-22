from fastapi import FastAPI
from src.controllers.products_controller import router as products_router

app = FastAPI(title="Products Service")

app.include_router(products_router, prefix="/products")
