# Representa que info puede recibir o devolver fast api

from pydantic import BaseModel

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    genero: str | None = None
    anio: int | None = None
    estado: str
    calificacion: int | None = None

    