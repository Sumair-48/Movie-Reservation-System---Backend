from fastapi import APIRouter, status, HTTPException
from typing import List
from Model import Pydantic_Model
from utils import dependencies
from Controller import Auth_control


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/sign_up",
             response_model=List[Pydantic_Model.User_response], 
             status_code=status.HTTP_200_OK)

async def sign_up(sign : Pydantic_Model.Sign_up, db : dependencies.db_dependency):
    user = Auth_control.sign_func(sign, db)
    if not user:
        raise HTTPException(status_code=400, detail="User creation failed")

    return [Pydantic_Model.User_response(**sign.dict())]


@router.get("/user/sign_in", 
            response_model=List[Pydantic_Model.Sign_in], 
            status_code=status.HTTP_302_FOUND)

async def user_acc(Email:str,password:str, db: dependencies.db_dependency):
    user = Auth_control.get_user_acc(Email,password,db)
    return [user]
