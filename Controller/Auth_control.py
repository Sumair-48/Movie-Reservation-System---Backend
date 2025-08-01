from Model import Database_Model, Pydantic_Model
from fastapi import HTTPException, status
from datetime import timedelta, datetime
from jose import  jwt, JWTError, ExpiredSignatureError
from Config import secret_key, algorithm, refresh_key

#Register Fundtion

def sign_func(x,db):
    sign_up = Database_Model.User(**x.model_dump())
    db.add(sign_up)
    db.commit()
    db.refresh(sign_up)
    return sign_up

def get_user_acc(Email,password,db):
    user_acc = db.query(Database_Model.User).filter(Database_Model.User.Email == Email).first()

    if not user_acc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not found!!")

    if Pydantic_Model.Hash.verify_pass(password, user_acc.password):
        return user_acc
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password!")
    

def create_access_token(username:str, user_id:int,is_admin:bool, expires_delta: timedelta):
    role = "admin" if is_admin == 1 else "user"
    encode = {'sub': username, 'id':user_id, 'role':role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    access_token = jwt.encode(encode,secret_key,algorithm)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
def create_refresh_token(username:str, user_id:int, is_admin:bool, expires_delta: timedelta):
    role = "admin" if is_admin == 1 else "user"
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    refresh_token = jwt.encode(encode, refresh_key, algorithm)
    return refresh_token


def verify_refresh_token(token:str):
    try:
        payload = jwt.decode(token, refresh_key, algorithms=[algorithm])
        user_id = payload.get("sub")
        if user_id is None:
            raise ValueError("Invalid token payload")
        return payload
    except ExpiredSignatureError:
        raise Exception("Refresh token has expired")
    except JWTError:
        raise Exception("Invalid refresh token")