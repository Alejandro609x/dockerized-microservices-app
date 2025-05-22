from fastapi import APIRouter, HTTPException
from typing import List
from src.dtos.user_dto import UserDTO

router = APIRouter()

users_db = []
user_id_seq = 1

@router.get("/", response_model=List[UserDTO])
async def get_users():
    return users_db

@router.get("/{user_id}", response_model=UserDTO)
async def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=UserDTO, status_code=201)
async def create_user(user: UserDTO):
    global user_id_seq
    new_user = user.dict()
    new_user["id"] = user_id_seq
    user_id_seq += 1
    users_db.append(new_user)
    return new_user

@router.put("/{user_id}", response_model=UserDTO)
async def update_user(user_id: int, updated_user: UserDTO):
    for idx, user in enumerate(users_db):
        if user["id"] == user_id:
            updated_data = updated_user.dict()
            updated_data["id"] = user_id
            users_db[idx] = updated_data
            return updated_data
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    for idx, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="User not found")
