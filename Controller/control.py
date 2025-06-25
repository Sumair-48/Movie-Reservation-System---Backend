from ..Model import Database_Model
from .. Model import Pydantic_Model


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
    password = Pydantic_Model.pwt_cxt.hash(password)
    user_acc = db.query(Database_Model.User).filter(
        Database_Model.User.Email == Email and 
        Database_Model.User.password == password
        ).first()
    return user_acc