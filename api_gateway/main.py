# Importación de librerías necesarias para FastAPI, validación de datos, HTTP, CSV y logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import httpx
import csv
import os
import logging

# Configura el nivel de logging a INFO para mostrar eventos importantes durante la ejecución
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Instancia de FastAPI con metadatos descriptivos
app = FastAPI(
    title="API Gateway - Productos y Usuarios",
    description="Este API Gateway conecta microservicios de productos y usuarios, y expone funciones agrupadas por secciones.",
    version="1.0.0"
)

# Modelos de datos para productos y usuarios (como lo ves en la pagian de api sin esto no vas a podes meter datos)
class Product(BaseModel):
    id: int = 0
    name: str
    price: float
    description: str

class User(BaseModel):
    id: int = 0
    first_name: str
    last_name: str
    email: str

# URLs base para conectar con los microservicios de productos y usuarios
PRODUCTS_URL = "http://products_service:8000"
USERS_URL = "http://users_service:8000"

# Ruta absoluta del CSV que será compartido con el contenedor del API Gateway
CSV_PATH = "/volumes/shared_csv/users.csv"

# Cliente HTTP asíncrono reutilizable para peticiones a microservicios
async def make_request(method: str, url: str, **kwargs):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(method, url, **kwargs)
            logger.info(f"Request to {url} - Status: {response.status_code}")

            # Manejo de redirecciones 307 (temporal redirect)
            if response.status_code == 307:
                redirect_url = response.headers.get('Location')
                if redirect_url:
                    logger.info(f"Following redirect to {redirect_url}")
                    return await client.request(method, redirect_url, **kwargs)

            return response
        except httpx.ConnectError:
            logger.error(f"Connection error to {url}")
            raise HTTPException(status_code=502, detail="Service unavailable")
        except Exception as e:
            logger.error(f"Error in request: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")

# --- PRODUCTOS ---

# Crear producto
@app.post("/products/", response_model=dict, tags=["Productos"])
async def create_product(product: Product):
    url = f"{PRODUCTS_URL}/products/"
    response = await make_request("POST", url, json=product.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Obtener todos los productos
@app.get("/products/", response_model=List[Product], tags=["Productos"])
async def get_products():
    url = f"{PRODUCTS_URL}/products/"
    response = await make_request("GET", url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Obtener producto por ID
@app.get("/products/{product_id}", response_model=Product, tags=["Productos"])
async def get_product(product_id: int):
    url = f"{PRODUCTS_URL}/products/{product_id}"
    response = await make_request("GET", url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Actualizar producto
@app.put("/products/{product_id}", response_model=dict, tags=["Productos"])
async def update_product(product_id: int, product: Product):
    url = f"{PRODUCTS_URL}/products/{product_id}"
    response = await make_request("PUT", url, json=product.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Eliminar producto
@app.delete("/products/{product_id}", response_model=dict, tags=["Productos"])
async def delete_product(product_id: int):
    url = f"{PRODUCTS_URL}/products/{product_id}"
    response = await make_request("DELETE", url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# --- USUARIOS ---

# Crear usuario y guardar en CSV
@app.post("/users/", response_model=dict, tags=["Usuarios"])
async def create_user(user: User):
    url = f"{USERS_URL}/users/"
    response = await make_request("POST", url, json=user.dict())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    save_user_to_csv(user)  # Guardar en CSV local compartido
    return response.json()

# Obtener todos los usuarios
@app.get("/users/", response_model=List[User], tags=["Usuarios"])
async def get_users():
    url = f"{USERS_URL}/users/"
    response = await make_request("GET", url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Obtener usuario por ID
@app.get("/users/{user_id}", response_model=User, tags=["Usuarios"])
async def get_user(user_id: int):
    url = f"{USERS_URL}/users/{user_id}"
    response = await make_request("GET", url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Actualizar usuario y CSV
@app.put("/users/{user_id}", response_model=dict, tags=["Usuarios"])
async def update_user(user_id: int, user: User):
    url = f"{USERS_URL}/users/{user_id}"
    response = await make_request("PUT", url, json=user.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    await rewrite_csv_with_users()  # Reescribir el CSV con todos los usuarios
    return response.json()

# Eliminar usuario y actualizar CSV
@app.delete("/users/{user_id}", response_model=dict, tags=["Usuarios"])
async def delete_user(user_id: int):
    url = f"{USERS_URL}/users/{user_id}"
    response = await make_request("DELETE", url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    await rewrite_csv_with_users()
    return response.json()

# --- CSV ---

# Obtener contenido del archivo CSV
@app.get("/csv/users/", tags=["CSV"])
async def get_users_csv():
    if not os.path.isfile(CSV_PATH):
        raise HTTPException(status_code=404, detail="CSV not found")
    with open(CSV_PATH, mode='r', encoding='utf-8') as f:
        content = f.read()
    return {"csv_content": content}

# Guardar un usuario en el archivo CSV
def save_user_to_csv(user: User):
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)  # Crea directorio si no existe
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["first_name", "last_name", "email"])
        if not file_exists:
            writer.writeheader()  # Escribe encabezados si el archivo es nuevo
        writer.writerow(user.dict())  # Escribe fila del usuario

# Reescribe el archivo CSV con todos los usuarios actuales
async def rewrite_csv_with_users():
    url = f"{USERS_URL}/users/"
    response = await make_request("GET", url)
    if response.status_code != 200:
        return
    users = response.json()
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    with open(CSV_PATH, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["first_name", "last_name", "email"])
        writer.writeheader()
        for u in users:
            writer.writerow(u)
