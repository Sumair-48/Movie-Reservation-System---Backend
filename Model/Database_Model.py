from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, PrimaryKeyConstraint, func, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, DATE, BOOLEAN, DATETIME, FLOAT, TIME
from datetime import datetime
from sqlalchemy.orm import relationship

BASE = declarative_base()


class User(BASE):
    __tablename__ = "User_table"

    ID = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
        )
    Name = Column(
        String(50),
        nullable=False,
        index=True
        )
    Phone = Column(
        String(11),
        unique=True,
        nullable=False
        )
    Email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
        )
    password = Column(
        String(70),
        nullable=False
        )
    is_admin = Column(
        BOOLEAN,
        default=False,
        nullable=False
        )

    reservations = relationship("Reservation", back_populates="user")

class Movie(BASE):
    __tablename__ = "Movie_Table"

    ID = Column(
        INTEGER(unsigned=True),
        autoincrement=True,
        nullable=False,
        unique=True
        )
    Title = Column(
        String(25),
        nullable=False,
        unique=True
        )
    Genre = Column(
        String(20),
        nullable=False
        )
    Duration = Column(
        INTEGER(unsigned=True),
        nullable=False
        )
    Language = Column(
        String(25),
        nullable=False
        )
    Rating = Column(
        String(20),
        nullable=False
        )
    Re_Date = Column(
        DATE,
        nullable=False
        )
    Description = Column(
        String(100),
        nullable=False
        )
    PrimaryKeyConstraint(ID,Title)
    showtimes = relationship("Showtime", back_populates="movie",foreign_keys="[Showtime.Movie_ID]")

class Screen(BASE):
    __tablename__ = "Screens"

    ID = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
        )
    Name = Column(
        String(20),
        unique=True,
        nullable=True
        )

    seats = relationship("Seats", back_populates="screen")
    showtimes = relationship("Showtime", back_populates="screen")

class Seats(BASE):
    __tablename__ = "Seats"

    ID = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
        )
    Screen_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Screens.ID"),
        nullable=False
        )
    Showtime_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Showtime.ID"),
        nullable=False
        )
    Seat_number = Column(
        String(20),
        nullable=False
        )

    screen = relationship("Screen", back_populates="seats")
    reservation_seats = relationship("Reservation_Seat", back_populates="seat")

class Showtime(BASE):
    __tablename__ = "Showtime"

    ID = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
        )
    Movie_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Movie_Table.ID"),
        nullable=False
        )
    Movie_name = Column(
        String(25),
        ForeignKey("Movie_Table.Title"),
        unique=True,
        nullable= False
    )
    Screen_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Screens.ID"),
        nullable=False
        )
    Start_time = Column(
        TIME,
        nullable=False,
        unique= True
        )
    End_time = Column(
        TIME,
        nullable= False,
        unique= True
    )
    Show_date = Column(
        DATE,
        nullable= False
    )

    movie = relationship("Movie", back_populates="showtimes",foreign_keys="[Showtime.Movie_ID]")
    screen = relationship("Screen", back_populates="showtimes")
    reservations = relationship("Reservation", back_populates="showtime")

class Reservation(BASE):
    __tablename__ = "Reservation"

    ID = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
        )
    User_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("User_table.ID"),
        nullable=False
        )
    Showtime_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Showtime.ID"),
        nullable=False
        )
    Created_at = Column(
        DATETIME,
        default=datetime.utcnow,
        nullable=False
        )
    Total_price = Column(
        FLOAT,
        default=1000,
        nullable=False
        )
    Status = Column(
        String(20),
        default="confirmed",
        nullable=False
        )

    user = relationship("User", back_populates="reservations")
    showtime = relationship("Showtime", back_populates="reservations")
    reservation_seats = relationship("Reservation_Seat", back_populates="reservation")

class Reservation_Seat(BASE):
    __tablename__ = "Reservated_Seats"

    ID = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
        )
    Reservation_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Reservation.ID"),
        nullable=False
        )
    Seat_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Seats.ID"),
        nullable=False
        )
    Showtime_ID = Column(
        INTEGER(unsigned=True),
        ForeignKey("Showtime.ID"),
        nullable=False
        )

    reservation = relationship("Reservation", back_populates="reservation_seats")
    seat = relationship("Seats", back_populates="reservation_seats")
    showtime = relationship("Showtime")
