from fastapi import FastAPI
from src.controllers.users_controller import router as users_router

app = FastAPI(title="Users Service")

app.include_router(users_router, prefix="/users")
