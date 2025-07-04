from fastapi import FastAPI
from .connection import engine
from .Model import Database_Model
from .routes import routes
from contextlib import asynccontextmanager

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting.....")
    Database_Model.BASE.metadata.create_all(engine)
    yield
    print("Server has been shutdown")



app = FastAPI (
    title = "CineVerse",
    description = "Movie Reservation System",
    lifespan= life_span
)

app.include_router(routes.router)