# Importamos BaseModel para definir modelos de datos y EmailStr para validar emails
from pydantic import BaseModel, EmailStr

# Definimos un modelo de datos para un usuario
class UserDTO(BaseModel):
    id: int = None  # Identificador del usuario, se asigna automáticamente (opcional al crear)
    first_name: str  # Nombre del usuario, obligatorio
    last_name: str   # Apellido del usuario, obligatorio
    email: EmailStr  # Correo electrónico del usuario, validado automáticamente como email válido
