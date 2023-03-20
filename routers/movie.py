from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movies import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieServices
from schemas.movie import Movie

movie_router = APIRouter()


# Para llamar a todas las peliculas y solocita el token


@movie_router.get('/movies', tags=['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    resultad = MovieServices(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(resultad))


# Para buscar por un ID
@movie_router.get('/movies/{id}', tags=['Movies'], response_model=Movie)
def get_movies_id(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    resultad = MovieServices(db).get_movie(id)
    if not resultad:
        return JSONResponse(status_code=404, content={
            'message': "No se ha encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(resultad))


# Para buscar por una categoria
@movie_router.get('/movies/', tags=['Movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieServices(db).get_movies_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# Para crear una pelicula
@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieServices(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})


# Para actualizar alguna pelicula
@movie_router.put('/movies', tags=['Movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Pelicula no encontrada"})
    MovieServices(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha actualizado la pelicula"})


# Para eliminar una peliciula
@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Pelicula no encontrada"})
    MovieServices(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la pelicula"})
