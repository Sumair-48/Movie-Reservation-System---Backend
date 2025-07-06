from Model import Database_Model

# Movies 

def movies(db):
    return db.query(Database_Model.Movie).all()