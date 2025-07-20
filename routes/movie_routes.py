from fastapi import APIRouter, status, HTTPException
from typing import List, Optional
from Model import Pydantic_Model
from utils import dependencies
from Controller import Movie_control
from Model import Database_Model

router = APIRouter(prefix="/movie", tags=["Movie"])

@router.get(
    "/filter/",
    response_model=List[Pydantic_Model.Movie_response],
    status_code=status.HTTP_200_OK
)
async def get_all_movies(db: dependencies.db_dependency):
    return Movie_control.movies(db)

# Get Movies 

@router.get("/{movie_name}/",
            response_model=Pydantic_Model.Movie_response,
            status_code=status.HTTP_302_FOUND)

async def get_movie(movie_name:str, db:dependencies.db_dependency):

    get_film = Movie_control.get_a_movie(movie_name,db)

    if not get_film:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Movie not found")
    return get_film



@router.get("/movies_filter",
            response_model=List[Pydantic_Model.Movie_response],
            status_code=status.HTTP_302_FOUND)

async def movie_filter(
    *, # serach all the arguments pass in this function 
    genre: Optional[str] = None,
    language: Optional[str] = None,
    db: dependencies.db_dependency
):
    query = db.query(Database_Model.Movie)

    if not genre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{genre} not found")
    query = Movie_control.get_genre(db, genre)

    if not language:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{language} not found")
    query = Movie_control.get_language(db, language)

    return query.all()



