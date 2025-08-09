from fastapi import APIRouter, status, HTTPException
from typing import List
from Model import Pydantic_Model
from utils import dependencies
from Controller import Admin_control


router = APIRouter(prefix="/admin", tags=["Admin"])

# Get all the users 

@router.get("/get_all_users",
            response_model=List[Pydantic_Model.User_response], 
            status_code=status.HTTP_200_OK)

async def get_all_users(db:dependencies.db_dependency, current_user:dependencies.user_dependency):

    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Only Admin Can Access")
    
    get_all = await Admin_control.get_users(db)

    if not get_all:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Could not get all the users")
    return get_all

# Screens

@router.get("/screens",
            response_model=List[Pydantic_Model.Screen_response],
            status_code=status.HTTP_200_OK)

async def view_screens(db:dependencies.db_dependency, current_user: dependencies.user_dependency):

    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Only Admin Can Access")
    
    get_screen = await Admin_control.get_screens(db)
    if not get_screen:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Could not get screens")
    return get_screen

# Add movies

@router.post("/add_movies/",
             response_model=Pydantic_Model.Movie_response,
             status_code=status.HTTP_200_OK)

async def add_Movies(movie_model: Pydantic_Model.Movie_response,
                db:dependencies.db_dependency,
                current_user: dependencies.user_dependency):
    
    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Only Admin Can Access")
    
    movies = await Admin_control.add_new_movies(movie_model,db)
    if not movies:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail= "Could not add the movies")
    return movies

# Add Show time

@router.post("/add_showtime", response_model=Pydantic_Model.Showtime,
             status_code=status.HTTP_200_OK)

async def showtime(request:Pydantic_Model.Showtime,
                   db: dependencies.db_dependency,
                   current_user: dependencies.user_dependency):
    
    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Only Admin Can Access")
    
    add_film_showtime = await Admin_control.add_show_time(request,db)

    if not add_film_showtime:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Showtime does not add")
    return add_film_showtime

# Update movie details

@router.patch("/update_movie/{movie_name}",
              response_model=Pydantic_Model.Movie_response_patch,
              status_code=status.HTTP_200_OK)

async def update_movie(movie_name:str,
                       request: Pydantic_Model.Movie_response_patch,
                        db:dependencies.db_dependency,
                        current_user: dependencies.user_dependency):
    
    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Only Admin Can Access")
    
    movie_data_update = await Admin_control.update_movie(movie_name,request,db)

    if not movie_data_update:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Could to update movie")
    return movie_data_update

@router.patch("/update_showtime/{id}",
              response_model=Pydantic_Model.get_showtime,
              status_code=status.HTTP_200_OK)

async def update_showtime (showtime_id:int,
                           request: Pydantic_Model.patch_showtime,
                           db: dependencies.db_dependency,
                           current_user: dependencies.user_dependency):
    
    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Only Admin Can Access")
    
    update_showtime = await Admin_control.update_showtime(showtime_id, request,db)
    
    if not update_showtime:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Could not update showtime")
    return update_showtime


# delete Movie

@router.delete("/delete_movie/{id}",
               status_code=status.HTTP_200_OK)

async def delete_movie(id:int, db:dependencies.db_dependency, current_user: dependencies.user_dependency):
    
    if current_user["role"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Only Admin Can Access")
    delete_film = await Admin_control.delete_a_movie(id,db)
    if not delete_film:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"movie id {id} not found")
    return delete_film
