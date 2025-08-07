from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.auth_routes import router as auth_router
from routes.admin_routes import router as admin_router
from routes.movie_routes import router as movie_router
from routes.user_routes import router as user_router
from init_db import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting.....")
    yield
    print("Server has been shutdown")


app = FastAPI (
    title = "CineVerse",
    description = "Movie Reservation System",
    lifespan= life_span
)


app.include_router(auth_router, prefix="/api/v1")
app.include_router(admin_router, prefix="/api/v1")
app.include_router(movie_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")
