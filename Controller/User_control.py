from fastapi import HTTPException, status
from Model import Database_Model, Pydantic_Model

# User Account details

def get_user_details(email,db):
    get_user = db.query(Database_Model.User).filter(Database_Model.User.Email == email).first()
    return get_user


def change_account(email,request,db):
    query = db.query(Database_Model.User).filter(Database_Model.User.Email == email).first()
    update_data = request.model_dump(exclude_unset = True)
    
    for field, values in update_data.items():
        setattr(query,field,values)

    db.commit()
    db.refresh(query)
    return query


def delete_user(email,db):
    query = db.query(Database_Model.User).filter(Database_Model.User.Email == email).first()
    db.delete(query)
    db.commit()
    return "Account has been deleted"