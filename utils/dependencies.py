from connection import SessionLocal
from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from Config import secret_key,algorithm, refresh_key
from jose import jwt, JWTError, ExpiredSignatureError

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token,secret_key,algorithms=[algorithm])
        username: str = payload.get('sub')
        user_id:int = payload.get('id')
        role:str = payload.get('role')
        if username is None or user_id is None or role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate the user")
        return {'username':username, 'id':user_id, 'role':role}
    except ExpiredSignatureError:
        raise Exception("Token is Expired")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate the user")
    
user_dependency = Annotated[dict, Depends(get_current_user)]

