from fastapi import APIRouter, HTTPException
from typing import List
from src.dtos.product_dto import ProductDTO

router = APIRouter()

# Simulación de DB en memoria
products_db = []
product_id_seq = 1

@router.get("/", response_model=List[ProductDTO])
async def get_products():
    return products_db

@router.get("/{product_id}", response_model=ProductDTO)
async def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/", response_model=ProductDTO, status_code=201)
async def create_product(product: ProductDTO):
    global product_id_seq
    new_product = product.dict()
    new_product["id"] = product_id_seq
    product_id_seq += 1
    products_db.append(new_product)
    return new_product

@router.put("/{product_id}", response_model=ProductDTO)
async def update_product(product_id: int, updated_product: ProductDTO):
    for idx, product in enumerate(products_db):
        if product["id"] == product_id:
            updated_data = updated_product.dict()
            updated_data["id"] = product_id
            products_db[idx] = updated_data
            return updated_data
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{product_id}", status_code=204)
async def delete_product(product_id: int):
    for idx, product in enumerate(products_db):
        if product["id"] == product_id:
            products_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Product not found")
