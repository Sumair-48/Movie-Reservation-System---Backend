from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List, Annotated
from Model import Pydantic_Model
from utils import dependencies
from Controller import Auth_control
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Auth"])

#Registeration Of User

@router.post("/sign_up/user",
             response_model=List[Pydantic_Model.User_response], 
             status_code=status.HTTP_200_OK)

async def sign_up_user(sign : Pydantic_Model.Sign_up, db : dependencies.db_dependency):
    user = Auth_control.sign_func(sign, db)
    if not user:
        raise HTTPException(status_code=400, detail="User creation failed")

    return [Pydantic_Model.User_response.model_validate(user)]


# Regestration Of Admin

@router.post("/sign_up/admin",
             response_model=List[Pydantic_Model.User_response], 
             status_code=status.HTTP_200_OK)

async def sign_up_admin(sign : Pydantic_Model.Sign_up_admin, db : dependencies.db_dependency):
    user = Auth_control.sign_func(sign, db)
    if not user:
        raise HTTPException(status_code=400, detail="User creation failed")

    return [Pydantic_Model.User_response.model_validate(user)]

# Login form 

@router.post("/token",
             response_model=Pydantic_Model.Token,
             status_code=status.HTTP_200_OK)

async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                  db: dependencies.db_dependency):
    user = Auth_control.get_user_acc(form_data.username,form_data.password,db)
    access_token = Auth_control.create_access_token(user.Email,user.ID,user.is_admin,timedelta(minutes=20))
    refresh_token = Auth_control.create_refresh_token(user.Email, user.ID, user.is_admin, timedelta(days=7))
    return {
        "access_token": access_token["access_token"],
        "token_type": access_token["token_type"],
        "refresh_token": refresh_token
    }
