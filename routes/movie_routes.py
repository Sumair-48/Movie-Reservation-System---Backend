from fastapi import APIRouter, status
from typing import List
from Model import Pydantic_Model
from utils import dependencies
from Controller import Movie_control

router = APIRouter(prefix="/movie", tags=["Movie"])

@router.get(
    "/filter/",
    response_model=List[Pydantic_Model.Movie_response],
    status_code=status.HTTP_200_OK
)
async def get_all_movies(db: dependencies.db_dependency):
    return Movie_control.movies(db)


@router.get("/{movie_name}/",
            response_model=Pydantic_Model.Movie_response,
            status_code=status.HTTP_302_FOUND)

async def get_movie(movie_name:str, db:dependencies.db_dependency):
    get_film = Movie_control.get_a_movie(movie_name,db)
    return get_film