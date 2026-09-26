from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from database import engine, get_db
import models
from schemas import LibroCreate

app = FastAPI() 

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

@app.get("/libros")
def obtener_libros(db: Session = Depends(get_db)):
    libros = db.query(models.Libro).all()
    return libros

@app.post("/libros")
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    nuevo_libro = models.Libro(
        titulo=libro.titulo,
        autor=libro.autor,
        genero=libro.genero,
        anio=libro.anio,
        estado=libro.estado,
        calificacion=libro.calificacion
    )
    
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

