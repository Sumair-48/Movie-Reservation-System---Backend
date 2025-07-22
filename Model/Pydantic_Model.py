from pydantic import BaseModel, Field, field_validator
from typing import Optional
from passlib.context import CryptContext
from datetime import date, datetime, time

pwt_cxt = CryptContext(schemes=['bcrypt'], deprecated = "auto")

# Hash class

class Hash():
    def hash_pass(value):
        return pwt_cxt.hash(value)
    
    def verify_pass(value,hash_value):
        return pwt_cxt.verify(value,hash_value)
    
# Regestration class for User
    
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

# Regestration class for Admin
    
class Sign_up_admin(BaseModel):
    Name : str
    Phone : str = Field(...,min_length=10 ,max_length=11)
    Email : str
    password : str = Field(..., min_length= 8 ,max_length=14)
    is_admin : bool

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

 # User details

class User_response(BaseModel):
    ID : int
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
    
#Movie response model   

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

# for Patch Update response model

class Movie_response_patch(BaseModel):
    Title : Optional[str] = None
    Genre : Optional[str] = None
    Duration : Optional[int] = None
    Language : Optional[str] = None
    Rating : Optional[str] = None
    Re_Date : Optional[date] = None
    Description : Optional[str] = None

    class Config:
        from_attributes = True
        from_orm = True
# patch for user response


class User_response_patch_new(BaseModel):
    
    Name : Optional[str] = None
    Phone : Optional[str] = None
    Email : Optional[str] = None
    password : Optional[str] = None

# patch for user response

class User_response_patch(BaseModel):
    
    Name : Optional[str] = None
    Phone : Optional[str] = Field(default=None ,min_length=10 ,max_length=11)
    Email : Optional[str] = None
    password : Optional[str] = Field(default=None, min_length= 8 ,max_length=14)

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

# Screen Response Model

class Screen_response(BaseModel):
    ID : int
    Name : str

    class Config:
        from_attributes = True

# Access token

class Token(BaseModel):
    access_token : str
    token_type : str

    class Config:
        from_attributes = True


# Showtime response mode 

class Showtime(BaseModel):
    Movie_ID : int
    Movie_name : str
    Screen_ID : int
    Start_time : time
    End_time : time
    Show_date : date

    class Config:
        from_attributes = True


# showtime get response model

class get_showtime(BaseModel):
    Movie_name : str
    Screen_ID : int
    Start_time : time
    End_time : time
    Show_date : date

    class Config:
        from_attributes = True

# showtime patch response model

class get_showtime(BaseModel):
    Movie_name :Optional[str]= None
    Screen_ID : Optional[int]= None
    Start_time : Optional[time] = None
    End_time : Optional[time] = None
    Show_date : Optional[date] = None

    class Config:
        from_attributes = True