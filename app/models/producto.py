from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

class Producto(BaseModel):
    id: Optional[str]  # Usamos un string para almacenar ObjectId
    nombre: str
    precio: float
    category: Optional[str]  # Añadí esta propiedad para reflejar la categoría

    class Config:
        # Configuración para convertir ObjectId a string
        json_encoders = {
            ObjectId: str  # Convierte ObjectId a string cuando se convierte a JSON
        }
