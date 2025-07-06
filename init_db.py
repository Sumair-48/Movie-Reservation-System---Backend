from Model import Database_Model
from connection import engine

def init_db():
    Database_Model.BASE.metadata.create_all(engine)