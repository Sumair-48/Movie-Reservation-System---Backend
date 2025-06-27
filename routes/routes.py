from fastapi import APIRouter, status, HTTPException, Depends
from ..connection import SessionLocal
from typing import Annotated, List
from sqlalchemy.orm import Session
from ..Model.Pydantic_Model import Sign_up, User_response, Sign_in
from ..Model import Database_Model
from ..Controller.control import sign_func, get_users, get_user_acc

router = APIRouter(
    prefix="/v1"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

@router.post("/sign_up",
             response_model=List[User_response], 
             status_code=status.HTTP_200_OK,tags=["Create Account"])

async def sign_up(sign : Sign_up, db : db_dependency):
    user = sign_func(sign, db)
    if not user:
        raise HTTPException(status_code=400, detail="User creation failed")

    return [User_response(**sign.dict())]


@router.get("/get_all_users",
            response_model=List[User_response], 
            status_code=status.HTTP_200_OK,tags=["Get All The Users"])

async def get_all(db:db_dependency):
    get_all = get_users(db)
    return get_all

@router.get("/user/sign_in", 
            response_model=List[Sign_in], 
            status_code=status.HTTP_302_FOUND, tags=["Users Account"])

async def user_acc(Email:str,password:str, db: db_dependency):
    user = get_user_acc(Email,password,db)
    return [user]

