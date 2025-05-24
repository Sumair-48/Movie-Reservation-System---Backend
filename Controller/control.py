from ..Model import Database_Model

def sign_func(x,db):
    sign_up = Database_Model.User(**x.model_dump())
    db.add(sign_up)
    db.commit()
    db.refresh(sign_up)
    return sign_up