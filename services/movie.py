from models.movies import Movie as MovieModel
from schemas.movie import Movie


class MovieServices():

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()

        return result

    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()

        return result

    def get_movies_category(self, category):
        result = self.db.query(MovieModel).filter(
            MovieModel.category == category).all()

        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())

        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, id: int, data: Movie):
        movie_update = self.db.query(MovieModel).filter(
            MovieModel.id == id).first()

        movie_update.title = data.title
        movie_update.overview = data.overview
        movie_update.year = data.year
        movie_update.rating = data.rating
        movie_update.category = data.category
        self.db.commit()
        return

    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()

        self.db.commit()
        return
