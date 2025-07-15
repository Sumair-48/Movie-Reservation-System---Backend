from Model import Database_Model

# Movies 

def movies(db):
    return db.query(Database_Model.Movie).all()

def get_a_movie(movie_name,db):
    return db.query(Database_Model.Movie).filter(Database_Model.Movie.Title == movie_name).first()