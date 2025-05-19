from fastapi import APIRouter, status, HTTPException, Depends
from ..connection import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session


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