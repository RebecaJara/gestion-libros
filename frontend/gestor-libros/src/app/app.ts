import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { Libro } from './libro';
import { LibroService } from './services/libro';

@Component({
  imports: [RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = signal('gestor-libros');

  libros: Libro[] = [];

  constructor(private libroService: LibroService) {
    this.libroService.obtenerLibros().subscribe({
      next: (datos) => {
        console.log('Datos obtenidos:', datos);
        this.libros = datos;
        console.log('Libros:', this.libros);
      },
      error: (error) => {
        console.error('Error al obtener los libros:', error);
      }
    })
  }
}