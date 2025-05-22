# Importamos APIRouter para crear rutas específicas, HTTPException para manejar errores HTTP
from fastapi import APIRouter, HTTPException
# Importamos List para indicar que retornaremos una lista de objetos UserDTO
from typing import List
# Importamos el modelo UserDTO que define cómo es un usuario
from src.dtos.user_dto import UserDTO

# Creamos un router para agrupar las rutas relacionadas con usuarios
router = APIRouter()

# Simulamos una "base de datos" en memoria con una lista
users_db = []
# Secuencia para asignar IDs únicos a cada usuario nuevo
user_id_seq = 1

# Ruta GET para obtener todos los usuarios
@router.get("/", response_model=List[UserDTO])
async def get_users():
    return users_db  # Devuelve la lista completa de usuarios

# Ruta GET para obtener un usuario específico por ID
@router.get("/{user_id}", response_model=UserDTO)
async def get_user(user_id: int):
    # Buscamos el usuario con el ID indicado
    for user in users_db:
        if user["id"] == user_id:
            return user  # Si se encuentra, lo devolvemos
    # Si no se encuentra, lanzamos error 404
    raise HTTPException(status_code=404, detail="User not found")

# Ruta POST para crear un nuevo usuario
@router.post("/", response_model=UserDTO, status_code=201)
async def create_user(user: UserDTO):
    global user_id_seq
    new_user = user.dict()  # Convertimos el objeto UserDTO a diccionario
    new_user["id"] = user_id_seq  # Asignamos un ID único automático
    user_id_seq += 1  # Incrementamos el contador para el próximo usuario
    users_db.append(new_user)  # Agregamos el nuevo usuario a la "base de datos"
    return new_user  # Devolvemos el usuario creado

# Ruta PUT para actualizar un usuario existente por ID
@router.put("/{user_id}", response_model=UserDTO)
async def update_user(user_id: int, updated_user: UserDTO):
    for idx, user in enumerate(users_db):
        if user["id"] == user_id:
            updated_data = updated_user.dict()  # Convertimos el objeto a dict
            updated_data["id"] = user_id  # Aseguramos que el ID no cambie
            users_db[idx] = updated_data  # Reemplazamos el usuario viejo por el nuevo
            return updated_data  # Devolvemos el usuario actualizado
    raise HTTPException(status_code=404, detail="User not found")

# Ruta DELETE para borrar un usuario por ID
@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    for idx, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db.pop(idx)  # Eliminamos el usuario de la lista
            return  # Retornamos vacío (204 No Content)
    raise HTTPException(status_code=404, detail="User not found")

