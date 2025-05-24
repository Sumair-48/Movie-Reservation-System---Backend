from pydantic import BaseModel, Field
from typing import Optional
from passlib.context import CryptContext # type: ignore

pwt_cxt = CryptContext(schemes=['bycrpt'], deprecated = "auto")

class Hash():
    def hash_pass(value):
        return pwt_cxt.hash(value)
    
    def verify_pass(value,hash_value):
        return pwt_cxt.verify(value,hash_value)
    
class Sign_up(BaseModel):
    Name : str
    Phone : int = Field(..., ge=1000000000, le=9999999999)
    Email : str
    password : str = Field(..., max_length=14)

    class Config:
        orm_mode = True

class Sign_in(BaseModel):
    Email : str
    password : str = Field(...,max_length=14)

    

