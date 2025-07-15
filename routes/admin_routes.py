from fastapi import APIRouter, status
from typing import List
from Model import Pydantic_Model
from utils import dependencies
from Controller import Admin_control


router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/get_all_users",
            response_model=List[Pydantic_Model.User_response], 
            status_code=status.HTTP_200_OK)

async def get_all_users(db:dependencies.db_dependency):
    get_all = Admin_control.get_users(db)
    return get_all

@router.post("/add_movies/",
             response_model=Pydantic_Model.Movie_response,
             status_code=status.HTTP_200_OK)

def add_Movies(movie_model: Pydantic_Model.Movie_response, db:dependencies.db_dependency):
    movies = Admin_control.add_new_movies(movie_model,db)
    return movies

@router.patch("/update_movie/{movie_name}",
              response_model=Pydantic_Model.Movie_response_patch,
              status_code=status.HTTP_200_OK)

async def update_movie(movie_name:str,
                       request: Pydantic_Model.Movie_response_patch,
                        db:dependencies.db_dependency):
    movie_data_update = Admin_control.update_movie(movie_name,request,db)
    return movie_data_update

