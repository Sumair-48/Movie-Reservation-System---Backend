from ..Model import Database_Model

def sign_func(a,db):
    new_acc = Database_Model.User(**a.model_dump())
    db.add(new_acc)
    db.commit()
    db.refresh(new_acc)
    return new_acc