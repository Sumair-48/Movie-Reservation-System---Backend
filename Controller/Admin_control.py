from Model import Database_Model
from fastapi import HTTPException, status
from sqlalchemy.future import select
#Get all the user in the system

async def get_users(db):
    all_user = await db.execute(select(Database_Model.User))
    return all_user.scalars().all()

# Add New Movies

async def add_new_movies(y,db):
    new_movies = Database_Model.Movie(**y.model_dump())
    db.add(new_movies)
    await db.commit()
    await db.refresh(new_movies)
    return new_movies


async def update_movie(movie_name,request,db):
    update = await db.execute(select(Database_Model.Movie).where(Database_Model.Movie.Title == movie_name))

    movie = update.scalars().first()
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Could not found {movie_name}")

    update_film =  request.model_dump(exclude_unset = True)
    for field, values in update_film.items():
        setattr(update, field, values)

    await db.commit()
    await db.refresh(movie)
    return update

async def delete_a_movie(id,db):
    movie_delete = await db.execute(select(Database_Model.Movie).where(Database_Model.Movie.ID == id))

    result = movie_delete.scalars().first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Could not found movie id: {id}")
    db.delete(result)
    await db.commit()
    return "Movie has been deleted"

async def get_screens(db):
    result = await db.execute(select(Database_Model.Screen))
    return result.scalars().all()

async def add_show_time(request,db):
    add_showtime = Database_Model.Showtime(**request.model_dump())
    db.add(add_showtime)
    await db.commit()
    await db.refresh(add_showtime)
    return add_showtime

async def update_showtime(id,request,db):

    showtime = await db.query(Database_Model.Showtime).filter(Database_Model.Showtime.ID == id).first()
    showtime = await db.execute(select(Database_Model.Showtime).where(Database_Model.Showtime.ID == id))

    result = showtime.scalars().first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Showtime not found")
    
    showtime_update = request.model_dump(exclude_unset=True)

    for field, value in showtime_update.items():
        setattr(showtime, field, value)
    await db.commit()
    await db.refresh(result)
    return showtime