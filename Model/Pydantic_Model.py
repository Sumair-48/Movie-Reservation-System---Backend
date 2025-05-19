from pydantic import BaseModel, Field
from typing import Optional


class Sign_up(BaseModel):
    Name : str
    Phone : int = Field(..., ge=1000000000, le=9999999999)
    Email : str
    password : str = Field(..., max_length=14)

    class Config:
        orm_mode = True