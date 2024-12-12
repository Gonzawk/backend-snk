# app/models/producto.py
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

class Producto(BaseModel):
    id: Optional[str]  # Usamos un string para almacenar ObjectId
    nombre: str
    precio: float

    class Config:
        # Configuración para convertir ObjectId a string
        json_encoders = {
            ObjectId: str  # Convierte ObjectId a string cuando se convierte a JSON
        }
