from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, PrimaryKeyConstraint, func
from sqlalchemy.dialects.mysql import INTEGER, BIGINT, DATE

BASE = declarative_base()

class User(BASE):
    __tablename__ = "User_table"
    ID = Column(
        INTEGER(unsigned=True),
        autoincrement=True,
        nullable=False
        )
    Name = Column(
        String(50),
        nullable=False
        )
    Phone = Column(
        String(11),
        unique= True,
        nullable= False
        )      
    Email = Column(
        String(100),
        nullable=False
        )
    password = Column(
        String(70),
        nullable = False
        )
    __table_args__ = (
        PrimaryKeyConstraint(ID,Email),
    )
    

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
    
