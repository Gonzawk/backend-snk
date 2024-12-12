# app/schemas/categoria.py
from pydantic import BaseModel
from typing import List, Optional

# Clase base para la categoria
class CategoriaBase(BaseModel):
    category_name: str
    description: str

# Categoria para respuesta (incluye el id)
class Categoria(CategoriaBase):
    id: str  # Este es el id que se devolverá en lugar de _id

    class Config:
        orm_mode = True  # Para convertir los datos de la base de datos en objetos Pydantic

# Para crear una categoría, no necesitamos el campo id
class CategoriaCreate(CategoriaBase):
    pass
