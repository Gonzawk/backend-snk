from pydantic import BaseModel
from typing import Optional

class Categoria(BaseModel):
    id: Optional[str]  # MongoDB usa ObjectId, pero lo tratamos como string en Pydantic
    nombre: str

    class Config:
        # Configuración para convertir ObjectId a string
        json_encoders = {
            # MongoDB ObjectId to string conversion
            str: lambda v: str(v)
        }
