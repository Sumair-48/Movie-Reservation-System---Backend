from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes import routes
from init_db import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting.....")
    init_db()
    yield
    print("Server has been shutdown")


app = FastAPI (
    title = "CineVerse",
    description = "Movie Reservation System",
    lifespan= life_span
)

app.include_router(routes.router)