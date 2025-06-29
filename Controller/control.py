from ..Model import Database_Model
from .. Model import Pydantic_Model
from fastapi import HTTPException, status


def sign_func(x,db):
    sign_up = Database_Model.User(**x.model_dump())
    db.add(sign_up)
    db.commit()
    db.refresh(sign_up)
    return sign_up

def get_users(db):
    all_users = db.query(Database_Model.User).all()
    return all_users


def get_user_acc(Email,password,db):
    user_acc = db.query(Database_Model.User).filter(Database_Model.User.Email == Email).first()

    if not user_acc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not found!!")

    if Pydantic_Model.Hash.verify_pass(password, user_acc.password):
        return user_acc
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password!")
    
def movies(db):
    return db.query(Database_Model.Movie).all()
 

def add_new_movies(y,db):
    new_movies = Database_Model.Movie(**y.model_dump())
    db.add(new_movies)
    db.commit()
    db.refresh(new_movies)
    return new_movies
