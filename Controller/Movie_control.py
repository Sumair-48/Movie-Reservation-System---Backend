from Model import Database_Model
from sqlalchemy.future import select

# Movies 

async def movies(db):
    movie = await db.execute(select(Database_Model.Movie))
    return movie.scalars().all()

async def get_a_movie(movie_name,db):
    result = await db.execute(select(Database_Model.Movie).where(Database_Model.Movie.Title == movie_name))
    return result.scalars().first()

async def get_movie(db):
    result = await db.execute(select(Database_Model.Movie))
    return result.scalars().all()

async def get_genre(db, genre:str):
    query = await db.execute(select(Database_Model.Movie).where(Database_Model.Movie.Genre.ilike(f"%{genre}%")))
    return query.scalars().all()

async def get_language(db, language:str):
    query = await db.execute(select(Database_Model.Movie.Language.ilike(f"%{language}%")))
    return query.scalars().all()

async def get_showtime(db):
    showtime = await db.execute(select(Database_Model.Showtime))
    return showtime.scalars().all()

