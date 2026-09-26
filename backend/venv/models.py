from sqlalchemy import Column, Integer, String
from database import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    autor = Column(String(100), nullable=False)
    genero = Column(String(50), nullable=False)
    anio = Column(Integer)
    estado = Column(String(20), nullable=False)
    calificacion = Column(Integer)