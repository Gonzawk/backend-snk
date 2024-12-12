# app/schemas/producto.py
from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    model: str
    color: str
    img_url: str
    category: str  # Este campo se refiere al ObjectId de la categoría como una cadena (string)

class Producto(ProductoBase):
    id: str  # El campo id es el ObjectId de MongoDB convertido a string

    class Config:
        orm_mode = True

class ProductoCreate(ProductoBase):
    pass
