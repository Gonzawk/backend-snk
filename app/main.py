from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import categorias_router, productos_router

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Agregar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Ajusta el origen si es necesario (por ejemplo, frontend en localhost:3000)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir los routers en la aplicación
app.include_router(categorias_router)
app.include_router(productos_router)
