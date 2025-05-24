from fastapi import APIRouter, status, HTTPException, Depends
from ..connection import SessionLocal
from typing import Annotated, List
from sqlalchemy.orm import Session
from ..Model.Pydantic_Model import Sign_up
from ..Model import Database_Model
from ..Controller.control import sign_func

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

@router.post("/sign_up", response_model= List[Sign_up], status_code=status.HTTP_200_OK,tags=["Create Account"])
async def sign_up(sign : Sign_up, db : db_dependency):
    return [sign_func(sign,db)]
