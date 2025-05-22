# Importamos FastAPI para crear la aplicación web
from fastapi import FastAPI
# Importamos el router que contiene las rutas relacionadas con usuarios
from src.controllers.users_controller import router as users_router

# Creamos una instancia de FastAPI y le damos un título a nuestro servicio
app = FastAPI(title="Users Service")

# Registramos las rutas de usuarios con el prefijo "/users"
# Esto significa que todas las rutas definidas en users_router estarán bajo la URL /users
app.include_router(users_router, prefix="/users")
