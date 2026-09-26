import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Libro } from '../libro';

@Injectable({
    providedIn: 'root'
})
export class LibroService {

    private apiUrl = 'http://localhost:8000/libros'; // URL de la API

    constructor(private http: HttpClient) { 

    }

    obtenerLibros() {
        return this.http.get<Libro[]>(this.apiUrl);
    }

}

