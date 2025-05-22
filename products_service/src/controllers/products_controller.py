# Importamos APIRouter para crear rutas específicas de productos
from fastapi import APIRouter, HTTPException
# Importamos List para especificar que una función retorna una lista de productos
from typing import List
# Importamos ProductDTO que es la estructura que define cómo es un producto (datos que tiene)
from src.dtos.product_dto import ProductDTO

# Creamos un router para agrupar las rutas relacionadas con productos
router = APIRouter()

# Simulamos una base de datos en memoria con una lista vacía
products_db = []

# Variable para asignar IDs únicos a cada producto nuevo
product_id_seq = 1

# Ruta para obtener todos los productos
@router.get("/", response_model=List[ProductDTO])
async def get_products():
    # Retornamos la lista completa de productos
    return products_db

# Ruta para obtener un producto específico por su ID
@router.get("/{product_id}", response_model=ProductDTO)
async def get_product(product_id: int):
    # Buscamos el producto en la "base de datos"
    for product in products_db:
        if product["id"] == product_id:
            # Si lo encontramos, lo retornamos
            return product
    # Si no lo encontramos, devolvemos un error 404
    raise HTTPException(status_code=404, detail="Product not found")

# Ruta para crear un nuevo producto
@router.post("/", response_model=ProductDTO, status_code=201)
async def create_product(product: ProductDTO):
    global product_id_seq
    # Convertimos el producto recibido a un diccionario
    new_product = product.dict()
    # Asignamos un ID único automático
    new_product["id"] = product_id_seq
    product_id_seq += 1
    # Agregamos el producto a la "base de datos"
    products_db.append(new_product)
    # Retornamos el producto creado con su ID asignado
    return new_product

# Ruta para actualizar un producto existente
@router.put("/{product_id}", response_model=ProductDTO)
async def update_product(product_id: int, updated_product: ProductDTO):
    # Buscamos el producto por su ID
    for idx, product in enumerate(products_db):
        if product["id"] == product_id:
            # Creamos un diccionario con los datos nuevos
            updated_data = updated_product.dict()
            # Nos aseguramos que el ID no cambie
            updated_data["id"] = product_id
            # Reemplazamos el producto antiguo con el actualizado
            products_db[idx] = updated_data
            # Retornamos el producto actualizado
            return updated_data
    # Si no encontramos el producto, devolvemos error 404
    raise HTTPException(status_code=404, detail="Product not found")

# Ruta para eliminar un producto
@router.delete("/{product_id}", status_code=204)
async def delete_product(product_id: int):
    # Buscamos el producto por su ID
    for idx, product in enumerate(products_db):
        if product["id"] == product_id:
            # Lo eliminamos de la lista
            products_db.pop(idx)
            # Retornamos sin contenido (204)
            return
    # Si no lo encontramos, error 404
    raise HTTPException(status_code=404, detail="Product not found")

