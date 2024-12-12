from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from pymongo.errors import PyMongoError


client = AsyncIOMotorClient("mongodb+srv://gdp43191989:Admin00@cluster0.t6n2s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["productos_catalogo"]

async def get_db():
    try:
        # Devolver la base de datos para cada solicitud
        yield db
    except PyMongoError as e:
        print(f"Error con la base de datos: {e}")
    finally:
        # Cerrar la conexión si es necesario (aunque Motor maneja el ciclo de vida)
        pass

 