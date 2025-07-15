from fastapi import APIRouter, HTTPException,status
from typing import List
from Model import Pydantic_Model
from utils import dependencies
from Controller import User_control

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/{email}",
            response_model=Pydantic_Model.User_response,
            status_code=status.HTTP_302_FOUND)
async def User_details(email:str, db:dependencies.db_dependency): # type: ignore
    get_user = User_control.get_user_details(email, db)
    return get_user