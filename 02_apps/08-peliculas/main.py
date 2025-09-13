from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Películas", version="1.0")

# Modelo de película
class Pelicula(BaseModel):
    id: int
    titulo: str
    anio: int
    descripcion: str
    director: str

# Base de datos en memoria
peliculas_db: List[Pelicula] = [
    Pelicula(id=1, titulo="El Padrino", anio=1972, descripcion="Mafia y familia en Nueva York.", director="Francis Ford Coppola"),
    Pelicula(id=2, titulo="Pulp Fiction", anio=1994, descripcion="Historias entrelazadas de crimen en Los Ángeles.", director="Quentin Tarantino"),
    Pelicula(id=3, titulo="Inception", anio=2010, descripcion="Un ladrón roba secretos a través de los sueños.", director="Christopher Nolan"),
    Pelicula(id=4, titulo="The Matrix", anio=1999, descripcion="Un hacker descubre la realidad simulada.", director="Lana y Lilly Wachowski"),
    Pelicula(id=5, titulo="Fight Club", anio=1999, descripcion="Un oficinista forma un club secreto de peleas.", director="David Fincher"),
    Pelicula(id=6, titulo="Forrest Gump", anio=1994, descripcion="La vida extraordinaria de un hombre común.", director="Robert Zemeckis"),
    Pelicula(id=7, titulo="Gladiator", anio=2000, descripcion="Un general romano busca venganza.", director="Ridley Scott"),
    Pelicula(id=8, titulo="Interstellar", anio=2014, descripcion="Viaje espacial en busca de un nuevo hogar.", director="Christopher Nolan"),
    Pelicula(id=9, titulo="The Shawshank Redemption", anio=1994, descripcion="La esperanza en una prisión.", director="Frank Darabont"),
    Pelicula(id=10, titulo="The Dark Knight", anio=2008, descripcion="Batman enfrenta al Joker.", director="Christopher Nolan"),
]

# Endpoints CRUD

@app.get("/peliculas", response_model=List[Pelicula])
def listar_peliculas():
    return peliculas_db

@app.get("/peliculas/{pelicula_id}", response_model=Pelicula)
def obtener_pelicula(pelicula_id: int):
    pelicula = next((p for p in peliculas_db if p.id == pelicula_id), None)
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return pelicula

@app.post("/peliculas", response_model=Pelicula)
def crear_pelicula(pelicula: Pelicula):
    if any(p.id == pelicula.id for p in peliculas_db):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    peliculas_db.append(pelicula)
    return pelicula

@app.put("/peliculas/{pelicula_id}", response_model=Pelicula)
def actualizar_pelicula(pelicula_id: int, nueva_pelicula: Pelicula):
    for idx, p in enumerate(peliculas_db):
        if p.id == pelicula_id:
            peliculas_db[idx] = nueva_pelicula
            return nueva_pelicula
    raise HTTPException(status_code=404, detail="Película no encontrada")

@app.delete("/peliculas/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int):
    for idx, p in enumerate(peliculas_db):
        if p.id == pelicula_id:
            del peliculas_db[idx]
            return {"mensaje": "Película eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Película no encontrada")
