from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, PrimaryKeyConstraint, func, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, BIGINT, DATE, BOOLEAN, DATETIME, FLOAT
from datetime import datetime
from sqlalchemy.orm import relationship

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
    
    reservation = relationship("Reservation", back_populates="User")

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
    
    showtime = relationship("Showtime", back_populates="Movie")

# Screen table 

class Screen(BASE):
    __tablename__ = "Screens"

    ID = Column(
        INTEGER,
        primary_key=True,
        unique=True,
        nullable=False
    )
    Name = Column(
        String,
        unique=True,
        nullable= True
    )

    seats = relationship("Seat", back_populates="Screens")
    showtime = relationship("Showtime", back_populates="Screen")


# Showtime table

class Showtime(BASE):
    __tablename__ = "Showtime"
    
    ID = Column(
        INTEGER,
        autoincrement=True,
        nullable = False,
        unique= True
    )
    Movie_ID = Column(
        INTEGER,
        ForeignKey("Movie_Table.ID"),
        nullable= False
    )
    Start_time = Column(
        DATETIME,
        nullable= False
    )
    Screen = Column(
        String
    )
    
    movie = relationship("Movie", back_populates="Showtime")
    screen = relationship("Screen", back_populates="showtime")
    reservation = relationship("Reservation", back_populates="Showtime")

class Seats(BASE):
    __tablename__ = "Seats"

    ID = Column(
        INTEGER,
        primary_key= True,
        nullable= False,
        unique= True
    )
    Showtime_ID = Column(
        INTEGER,
        ForeignKey("Showtime.ID")
    )
    Seat_number = Column(
        String,
        nullable= False
    )

    screen = relationship("Screen", back_populates="Seats")
    reservation_seats = relationship("Reservation", back_populates="Seats")


class Reservation(BASE):
    __tablename__ = "Reservation"

    ID = Column(
        INTEGER,
        primary_key=True,
        unique= True,
        nullable= False
    )
    User_ID = Column(
        INTEGER,
        ForeignKey("User_Table.ID")
    )
    Showtime_ID = Column(
        INTEGER,
        ForeignKey("Showtime.ID")
    )
    Created_at = Column(
        DATETIME,
        default=datetime.utcnow
    )
    Total_price = Column(
        FLOAT,
        default=1000
    )
    Status = Column(
        String,
        default="confirmed"
    )

    user = relationship("User", back_populates="Reservation")
    showtime = relationship("Showtime", back_populates="Reservation")
    reservation_seats = relationship("Reservation_Seats", back_populates="Reservation")
    
class Reservation_Seat(BASE):
    __tablename__ = "Reservated_Seats"

    ID = Column(
        INTEGER,
        primary_key=True,
        unique=True,
        nullable= True
    )
    Reservation_ID = Column(
        INTEGER,
        ForeignKey("Reservation.ID")
    )
    Seat_ID = Column(
        INTEGER,
        ForeignKey("Seats.ID")
    )
    Showtime_ID = Column(
        INTEGER,
        ForeignKey("Reservation.ID"),
        nullable=False
    )
    
    reservation = relationship("Reservation", back_populates="Reservation_Seats")
    seat = relationship("Seats", back_populates="Reservation_Seats")
    showtime = relationship("Showtime")
    