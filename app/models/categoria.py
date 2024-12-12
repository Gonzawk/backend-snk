# app/models/categoria.py
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId  # Importa ObjectId desde bson

class Categoria(BaseModel):
    id: Optional[str]  # MongoDB usa ObjectId, pero lo tratamos como string en Pydantic
    nombre: str

    class Config:
        # Configuración para convertir ObjectId a string
        json_encoders = {
            ObjectId: str  # Convierte ObjectId a string cuando se convierte a JSON
        }
