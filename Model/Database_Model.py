from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, CheckConstraint, PrimaryKeyConstraint
from sqlalchemy.dialects.mssql import INTEGER, BIGINT

BASE = declarative_base()

class User(BASE):
    __tablename__ = "User_table"
    ID = Column(
        BIGINT(unsigned = True),
        autoincrement= True,
        nullable= False
        )
    Name = Column(
        String(50),
        nullable= False
        )
    Phone = Column(
        INTEGER(unsigned = True),
        unique= True,
        nullable= False
        )      
    Email = Column(
        String,
        nullable=False
        )
    password = Column(
        String(50),
        nullable = False
        )
    __table_arge__ = PrimaryKeyConstraint(ID,Email)

    