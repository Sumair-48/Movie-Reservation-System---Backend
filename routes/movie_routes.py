from fastapi import APIRouter, status
from typing import List
from Model import Pydantic_Model
from utils import dependencies
from Controller import Movie_control

router = APIRouter(prefix="/movie", tags=["Movie"])

@router.get(
    "/movies/filter/",
    response_model=List[Pydantic_Model.Movie_response],
    status_code=status.HTTP_200_OK
)
def movie_filter(db: dependencies.db_dependency):
    return Movie_control.movies(db)
