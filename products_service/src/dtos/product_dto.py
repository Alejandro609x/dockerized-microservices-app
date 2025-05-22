# Importamos BaseModel de Pydantic para crear modelos de datos con validación automática
from pydantic import BaseModel

# Definimos una clase llamada ProductDTO que representa un producto
class ProductDTO(BaseModel):
    # El id del producto, que es un número entero. Inicialmente puede ser None porque se asigna automáticamente luego.
    id: int = None  
    
    # El nombre del producto, es un texto obligatorio
    name: str  
    
    # El precio del producto, que debe ser un número decimal (float)
    price: float  
    
    # La descripción del producto, que puede ser un texto o estar vacía (None)
    description: str | None = None  
