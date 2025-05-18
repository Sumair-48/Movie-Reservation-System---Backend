from fastapi import FastAPI
from .connection import engine
from .Model import Database_Model

Database_Model.BASE.metadata.create_all(engine)

app = FastAPI()