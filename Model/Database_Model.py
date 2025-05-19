from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import INTEGER, BIGINT

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
        BIGINT(unsigned=True),
        unique= True,
        nullable= False
        )      
    Email = Column(
        String(100),
        nullable=False
        )
    password = Column(
        String(50),
        nullable = False
        )
    __table_args__ = (
        PrimaryKeyConstraint(ID,Email),
    )
    