from pydantic import BaseModel, Field
from typing import Optional


'''Este es el esquema de mi movie'''


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(Le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=25)

    class Config:
        schema_extra = {
            "example": {
                "title": "Mi pelicula",
                "overview": "Decripcion de la pelicula",
                "year": 2023,
                "rating": 9.8,
                "category": "Categoria de la pelicula"
            }
        }
