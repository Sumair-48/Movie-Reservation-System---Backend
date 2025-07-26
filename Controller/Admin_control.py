from Model import Database_Model
from fastapi import HTTPException, status

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
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Could not found {movie_name}")

    update_film = request.model_dump(exclude_unset = True)
    for field, values in update_film.items():
        setattr(update, field, values)

    db.commit()
    db.refresh(update)
    return update

def delete_a_movie(id,db):
    movie_delete = db.query(Database_Model.Movie).filter(Database_Model.Movie.ID == id).first()
    if not movie_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Could not found movie id: {id}")
    db.delete(movie_delete)
    db.commit()
    return "Movie has been deleted"

def get_screens(db):
    return db.query(Database_Model.Screen).all()


def add_show_time(request,db):
    add_showtime = Database_Model.Showtime(**request.model_dump())
    db.add(add_showtime)
    db.commit()
    db.refresh(add_showtime)
    return add_showtime

def update_showtime(id,request,db):

    showtime = db.query(Database_Model.Showtime).filter(Database_Model.Showtime.ID == id).first()
    if not showtime:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Showtime not found")
    showtime_update = request.model_dump(exclude_unset=True)
    for field, value in showtime_update.items():
        setattr(showtime, field, value)
    db.commit()
    db.refresh(showtime)
    return showtime