# app/routers/productos.py
from fastapi import APIRouter, Depends
from app.db import get_db
from app.schemas.producto import Producto
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List

router = APIRouter()

# Función para convertir _id de MongoDB a id
def convert_objectid(item):
    item['id'] = str(item['_id'])  # Convertimos _id a string en id
    del item['_id']  # Eliminamos el campo _id original
    item['category'] = str(item['category'])  # Convertimos category a string también
    return item

@router.get("/productos", response_model=List[Producto])
async def obtener_productos(db: AsyncIOMotorClient = Depends(get_db)):
    productos = await db.productos.find().to_list(length=None)

    # Convertimos cada producto para que incluya el campo id en lugar de _id y category a string
    productos_convertidos = [convert_objectid(producto) for producto in productos]

    return productos_convertidos
