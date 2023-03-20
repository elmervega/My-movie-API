from fastapi import FastAPI
from pydantic import BaseModel
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"


# Aqui llamamos a nuestro middleware para cuando exista errores
app.add_middleware(ErrorHandler)

# Llamos a nuestra conexion
Base.metadata.create_all(bind=engine)

# LLamo a mi router de la aplicacion
app.include_router(movie_router)

# Llamo a mi router de user
app.include_router(user_router)


movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Avatar 2',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    }
]
