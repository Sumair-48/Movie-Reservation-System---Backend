from pydantic import BaseModel, Field, field_validator
from typing import Optional
from passlib.context import CryptContext
from datetime import date

pwt_cxt = CryptContext(schemes=['bcrypt'], deprecated = "auto")

class Hash():
    def hash_pass(value):
        return pwt_cxt.hash(value)
    
    def verify_pass(value,hash_value):
        return pwt_cxt.verify(value,hash_value)
    
class Sign_up(BaseModel):
    Name : str
    Phone : str = Field(...,min_length=10 ,max_length=11)
    Email : str
    password : str = Field(..., min_length= 8 ,max_length=14)

    @field_validator("Phone", mode="before")
    def check_no(cls,value):
        value = str(value)

        if value.startswith("0"):
            value = value[1:]
        
        if not value.isdigit():
            raise ValueError("Phone number must be numeric")

        if len(value) != 10 :
            raise ValueError("Phone no length must be 10")
        
        return str(value)
    
    @field_validator("password",mode="after")
    def hash_pass(cls,value) -> str:
        if isinstance(value,str) and value.startswith("$2b$"):
            return value
        return pwt_cxt.hash(value)

    class Config:
        from_attributes = True

class User_response(BaseModel):
    Name : str
    Phone : str 
    Email : str

    class Config:
        from_attributes = True

class Sign_in(BaseModel):
    Name : str
    Phone : str
    Email : str
    
    class Config:
        from_attributes = True
    

class Movie_response(BaseModel):
    Title : str
    Genre : str
    Duration : int
    Language : str
    Rating : str
    Re_Date : date
    Description : str

    class Config:
        from_attributes = True
        from_orm = True