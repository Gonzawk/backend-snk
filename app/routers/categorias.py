from fastapi import APIRouter, Depends
from app.db import get_db
from app.schemas.categoria import Categoria
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List

router = APIRouter()

# Función que convierte _id de MongoDB a id
def convert_objectid(item):
    item['id'] = str(item['_id'])  # Convertimos _id a string en id
    del item['_id']  # Eliminamos el campo _id original
    return item

@router.get("/categorias", response_model=List[Categoria])
async def obtener_categorias(db: AsyncIOMotorClient = Depends(get_db)):
    categorias = await db.categorias.aggregate([
        {
            '$lookup': {
                'from': 'productos',  # Nombre de la colección de productos
                'localField': 'products',  # Campo en la categoría que contiene los ObjectIds
                'foreignField': '_id',  # Campo en productos que contiene los ObjectIds
                'as': 'productos_detalle'  # Alias donde se guardarán los resultados del join
            }
        },
        {
            '$project': {
                'category_name': 1,
                'description': 1,
                'productos_detalle.name': 1,  # Seleccionamos solo el nombre del producto
                'productos_detalle.description': 1  # También puedes seleccionar otros campos de producto
            }
        }
    ]).to_list(length=None)

    # Convertimos cada categoría para que incluya el campo id en lugar de _id
    categorias_convertidas = [convert_objectid(categoria) for categoria in categorias]

    return categorias_convertidas
