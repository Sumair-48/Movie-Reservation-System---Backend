from Model import Database_Model


#Get all the user in the system

def get_users(db):
    all_users = db.query(Database_Model.User).all()
    return all_users

# Add New Movies

def add_new_movies(y,db):
    new_movies = Database_Model.Movie(**y.model_dump())
    db.add(new_movies)
    db.commit()
    db.refresh(new_movies)
    return new_movies
