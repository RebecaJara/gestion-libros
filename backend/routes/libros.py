from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import models
from schemas import LibroCreate, LibroUpdate

router = APIRouter()


@router.get("/") 
def inicio():
    return {"mensaje": "Gestor de libros funcionando"}


@router.get("/conexion")
def comprobar_conexion():
    try:
        with engine.connect() as connection:
            return {"mensaje": "Conexión a la base de datos exitosa"}
    except Exception as e:
        return {"mensaje": "Error al conectar a la base de datos", "error": str(e)}


@router.get("/libros") #obtiene todos los libros
def obtener_libros(db: Session = Depends(get_db)):
    libros = db.query(models.Libro).all()
    return libros


@router.get("/libros/{libro_id}") #obtiene un libro por su id
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if libro is None:
        return {"mensaje": "Libro no encontrado"}
    return libro

    libro_existente.titulo = libro.titulo
    libro_existente.autor = libro.autor
    libro_existente.genero = libro.genero
    libro_existente.anio = libro.anio
    libro_existente.estado = libro.estado
    libro_existente.calificacion = libro.calificacion
    
    db.commit()
    db.refresh(libro_existente)
    return libro_existente


@router.put("/libros/{libro_id}")
def actualizar_libro(
    libro_id: int,
    libro_actualizado: LibroUpdate,
    db: Session = Depends(get_db)
):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()

    if libro is None:
        return {"mensaje": "Libro no encontrado"}

    libro.titulo = libro_actualizado.titulo
    libro.autor = libro_actualizado.autor
    libro.genero = libro_actualizado.genero
    libro.anio = libro_actualizado.anio
    libro.estado = libro_actualizado.estado
    libro.calificacion = libro_actualizado.calificacion

    db.commit()
    db.refresh(libro)

    return libro


@router.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    
    if libro is None:
        return {"mensaje": "Libro no encontrado"}
    
    db.delete(libro)
    db.commit()
    return {"mensaje": "Libro eliminado exitosamente"}


@router.post("/libros")
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
