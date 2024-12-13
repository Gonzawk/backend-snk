import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URI de MongoDB y el nombre de la base de datos desde las variables de entorno
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DATABASE_NAME")

# Conectar a MongoDB usando la URI y nombre de base de datos
client = AsyncIOMotorClient(mongo_uri)
db = client[db_name]

async def get_db():
    try:
        # Devolver la base de datos para cada solicitud
        yield db
    except PyMongoError as e:
        print(f"Error con la base de datos: {e}")
        raise e  # Lanza el error para que sea manejado más arriba en la pila de ejecución
