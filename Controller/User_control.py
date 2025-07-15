from fastapi import HTTPException, status
from Model import Database_Model, Pydantic_Model

# User Account details

def get_user_details(email,db):
    get_user = db.query(Database_Model.User).filter(Database_Model.User.Email == email).first()
    return get_user


    
