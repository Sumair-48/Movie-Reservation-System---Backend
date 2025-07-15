from Model import Database_Model

# Movies 

def movies(db):
    return db.query(Database_Model.Movie).all()

def get_a_movie(movie_name,db):
    return db.query(Database_Model.Movie).filter(Database_Model.Movie.Title == movie_name).first()

def get_movie(db):
    return db.query(Database_Model.Movie)

def get_genre(db, genre:str):
    query = db.query(Database_Model.Movie)
    query = query.filter(Database_Model.Movie.Genre.ilike(f"%{genre}%"))
    return query

def get_language(db, language:str):
    query = get_movie(db)
    query = query.filter(Database_Model.Movie.Language.ilike(f"%{language}%"))
    return query
