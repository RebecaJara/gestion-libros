export interface Libro {
  id: number;
  titulo: string;
  autor: string;
  genero: string | null;
  anio: number | null;
  estado: string;
  calificacion: number | null;
}