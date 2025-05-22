from pydantic import BaseModel, EmailStr

class UserDTO(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    email: EmailStr
