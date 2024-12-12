from app.database import db
from bson import ObjectId
from app.models import Categoria  # Asegúrate de tener el modelo Pydantic adecuado

# Función para convertir ObjectId en cadena (string)
def str_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

def get_categorias():
    categorias = db.categorias.find()
    categorias_list = []
    for categoria in categorias:
        categoria["_id"] = str_objectid(categoria["_id"])  # Convertir _id a string
        categorias_list.append(categoria)
    return categorias_list

def create_categoria(categoria):
    # Asegúrate de insertar los datos correctamente y devolver el ID como string
    categoria_data = dict(categoria)  # Convierte el modelo Pydantic en dict
    result = db.categorias.insert_one(categoria_data)
    categoria_data["id"] = str(result.inserted_id)  # Asignamos el ID generado a la respuesta
    return categoria_data
