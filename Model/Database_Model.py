from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mssql import INTEGER

BASE = declarative_base()

class User(BASE):
    __tablename__ = "User_details"
    ID = Column(
        INTEGER(unsigned = True),
        autoincrement= True,
        nullable= False
        )
    Name = Column(
        String(50),
        nullable= False
        )
    Email = Column(
        String,
        nullable=False
        )
    