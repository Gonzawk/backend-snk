from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import categorias_router, productos_router

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Agregar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontendd-snk.vercel.app",
        "https://web-production-4ea6.up.railway.app",  # Asegúrate de incluir el dominio de Railway
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluir los routers en la aplicación
app.include_router(categorias_router)
app.include_router(productos_router)
