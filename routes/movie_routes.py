from fastapi import APIRouter, status, HTTPException
from typing import List, Optional
from Model import Pydantic_Model
from utils import dependencies
from Controller import Movie_control
from Model import Database_Model
from sqlalchemy.future import select

router = APIRouter(prefix="/movie", tags=["Movie"])

@router.get(
    "/filter/",
    response_model=List[Pydantic_Model.Movie_response],
    status_code=status.HTTP_200_OK
)
async def get_all_movies(db: dependencies.db_dependency):
    result =  await Movie_control.movies(db)
    return result

# Get Movies 

@router.get("/{movie_name}/",
            response_model=Pydantic_Model.Movie_response,
            status_code=status.HTTP_302_FOUND)

async def get_movie(movie_name:str, db:dependencies.db_dependency):

    get_film = await Movie_control.get_a_movie(movie_name,db)

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
    query = await db.execute(select(Database_Model.Movie))


    if not genre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{genre} not found")
    query = await Movie_control.get_genre(db, genre)

    if not language:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{language} not found")
    query = await Movie_control.get_language(db, language)

    return query.scalars().all()


@router.get("/showtime",
            response_model=List[Pydantic_Model.get_showtime],
            status_code=status.HTTP_200_OK)

async def get_all_showtime(db:dependencies.db_dependency):
    get_all_films = await Movie_control.get_showtime(db)
    if not get_all_films:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Could not get showtime")
    return get_all_films