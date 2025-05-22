from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int = None  # será asignado automáticamente
    name: str
    price: float
    description: str | None = None
