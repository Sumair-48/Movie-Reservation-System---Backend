from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.auth_routes import router as auth_router
from routes.admin_routes import router as admin_router
from routes.movie_routes import router as movie_router
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


app.include_router(auth_router, prefix="/v1")
app.include_router(admin_router, prefix="/v1")
app.include_router(movie_router, prefix="/v1")