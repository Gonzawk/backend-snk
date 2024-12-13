import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# Configuración de la conexión
client = AsyncIOMotorClient("mongodb+srv://gdp43191989:Admin00@cluster0.t6n2s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Cambia la URL si tu base de datos está en otro servidor
db = client["productos_catalogo"]  # Cambia "nombre_base_de_datos" por el nombre de tu base de datos

async def probar_conexion():
    try:
        info = await db.command("ping")  # Comando de prueba para verificar la conexión
        print("Conexión exitosa:", info)
    except Exception as e:
        print("Error en la conexión:", e)

# Ejecuta la función de prueba
if __name__ == "__main__":
    asyncio.run(probar_conexion())
