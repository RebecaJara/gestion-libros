from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session # type: ignore
from database import engine, get_db
import models
from routes import libros
from schemas import LibroCreate, LibroUpdate

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(libros.router)

@app.get("/") 
def inicio():
    return {"mensaje": "Gestor de libros funcionando"}


@app.get("/conexion")
def comprobar_conexion():
    try:
        with engine.connect() as connection:
            return {"mensaje": "Conexión a la base de datos exitosa"}
    except Exception as e:
        return {"mensaje": "Error al conectar a la base de datos", "error": str(e)}
