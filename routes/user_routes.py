from fastapi import APIRouter,status, Depends
from Model import Pydantic_Model
from utils import dependencies
from Controller import User_control


router = APIRouter(prefix="/user", tags=["User"])

@router.get("/account_details/{email}",
            response_model=Pydantic_Model.User_response,
            status_code=status.HTTP_302_FOUND)

async def User_details(email:str, db:dependencies.db_dependency, current_user: dependencies.user_dependency): # type: ignore
    if current_user["role"] =="user":
        get_user = User_control.get_user_details(email, db)
        return get_user

@router.patch("/update_account/{email}",
              response_model=Pydantic_Model.User_response_patch,
              status_code=status.HTTP_200_OK)

async def update_account(email:str,
                         request:Pydantic_Model.User_response_patch,
                         db: dependencies.db_dependency):
    
    update = User_control.change_account(email,request,db)
    return update


@router.delete("/account_delete/{email}",
               status_code=status.HTTP_200_OK)

async def delete_account(email:str, db:dependencies.db_dependency):
    data = User_control.delete_user(email,db)
    return data