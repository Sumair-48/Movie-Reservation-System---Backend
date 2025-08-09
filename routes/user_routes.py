from fastapi import APIRouter,status, HTTPException
from Model import Pydantic_Model
from utils import dependencies
from Controller import User_control


router = APIRouter(prefix="/user", tags=["User"])

# Account Details 

@router.get("/account_details/{email}",
            response_model=Pydantic_Model.User_response,
            status_code=status.HTTP_302_FOUND)

async def User_details(email:str,
                       db:dependencies.db_dependency,
                       current_user: dependencies.user_dependency): # type: ignore
    
    if current_user["role"] != "user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail= "User Only Access")
    
    if current_user["username"] != email:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                            detail="Not Authorized user")
    
    get_user = await User_control.get_user_details(email,db)

    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    
    return get_user

# Update Account Detail

@router.patch("/update_account/{email}",
              response_model=Pydantic_Model.User_response_patch,
              status_code=status.HTTP_200_OK)

async def update_account(email:str,
                         request:Pydantic_Model.User_response_patch_new,
                         db: dependencies.db_dependency,
                         current_user: dependencies.user_dependency):
    
    if current_user["role"] !="user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="User Only Access")
    
    if current_user["username"] != email:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                            detail="Not Authorized User")
    
    update = await User_control.change_account(email,request,db)

    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return update

# Delete Account 

@router.delete("/account_delete/{email}",
               status_code=status.HTTP_200_OK)

async def delete_account(email:str, db:dependencies.db_dependency,
                         current_user: dependencies.user_dependency):
    
    if current_user["role"] =="user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="User Only Access")
    
    if current_user["username"] != email:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                            detail="Not Authorized User")

    data = await User_control.delete_user(email,db)
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return data