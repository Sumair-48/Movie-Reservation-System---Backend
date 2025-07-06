from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, PrimaryKeyConstraint, func
from sqlalchemy.dialects.mysql import INTEGER, BIGINT, DATE, BOOLEAN

BASE = declarative_base()

# User Table 

class User(BASE):
    __tablename__ = "User_table"
    ID = Column(
        INTEGER(unsigned=True),
        autoincrement=True,
        nullable=False
        )
    Name = Column(
        String(50),
        nullable=False,
        index= True
        )
    Phone = Column(
        String(11),
        unique= True,
        nullable= False
        )      
    Email = Column(
        String(100),
        nullable=False,
        index=True
        )
    password = Column(
        String(70),
        nullable = False
        )
    is_admin = Column(
        BOOLEAN,
        nullable=False,
        default=False
    )
    __table_args__ = (
        PrimaryKeyConstraint(ID,Email),
    )
    
#  Movie Table

class Movie(BASE):
    __tablename__ = "Movie_Table"
    ID = Column(
        BIGINT(unsigned=True),
        autoincrement = True,
        nullable= False,
        unique= True
        )
    Title = Column(
        String(25),
        nullable=False,
        unique= True
    )
    Genre = Column(
        String(20),
        nullable = False
    )
    Duration = Column(
        INTEGER(unsigned = True),
        nullable= False
    )
    Language = Column(
        String(25),
        nullable= False 
    )
    Rating = Column(
        String(20),
        nullable= False
    )
    Re_Date = Column(
        DATE,
        nullable= False
    )
    Description = Column(
        String(100),
        nullable = False
    )
    __table_args__ = (
        PrimaryKeyConstraint(ID,Title),
    )
    
