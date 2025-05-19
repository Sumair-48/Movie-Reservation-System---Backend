from fastapi import FastAPI
from .connection import engine
from .Model import Database_Model
from .routes import routes

Database_Model.BASE.metadata.create_all(engine)

app = FastAPI()

app.include_router(routes.router)