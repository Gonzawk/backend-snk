from app.database import db
from bson import ObjectId
from app.models import Producto  # Asegúrate de tener el modelo Pydantic adecuado

# Función para convertir ObjectId en cadena (string)
def str_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

def get_productos():
    productos = db.productos.find()
    productos_list = []
    for producto in productos:
        producto["_id"] = str_objectid(producto["_id"])  # Convertir _id a string
        productos_list.append(producto)
    return productos_list

def create_producto(producto):
    # Asegúrate de insertar los datos correctamente y devolver el ID como string
    producto_data = dict(producto)  # Convierte el modelo Pydantic en dict
    result = db.productos.insert_one(producto_data)
    producto_data["id"] = str(result.inserted_id)  # Asignamos el ID generado a la respuesta
    return producto_data
