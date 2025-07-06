from fastapi import APIRouter, status
from typing import List
from Model import Pydantic_Model
from utils import dependencies
from Controller import Admin_control


router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/get_all_users",
            response_model=List[Pydantic_Model.User_response], 
            status_code=status.HTTP_200_OK)

async def get_all(db:dependencies.db_dependency):
    get_all = Admin_control.get_users(db)
    return get_all

@router.post("/movies/",
             response_model=List[Pydantic_Model.Movie_response],
             status_code=status.HTTP_200_OK)

def add_Movies(movie_model: Pydantic_Model.Movie_response, db:dependencies.db_dependency):
    movies = Admin_control.add_new_movies(movie_model,db)
    return [movies]