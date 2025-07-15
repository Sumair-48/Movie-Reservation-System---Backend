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


def update_movie(movie_name,request,db):
    update = db.query(Database_Model.Movie).filter(Database_Model.Movie.Title == movie_name).first()
    update_film = request.model_dump(exclude_unset = True)
    for field, values in update_film.items():
        setattr(update, field, values)

    db.commit()
    db.refresh(update)
    return update

def delete_a_movie(id,db):
    movie_delete = db.query(Database_Model.Movie).filter(Database_Model.Movie.ID == id).first()
    db.delete(movie_delete)
    db.commit()
    return "Movie has been deleted"