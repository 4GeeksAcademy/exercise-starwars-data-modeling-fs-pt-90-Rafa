import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    name = Column(String(250), nullable=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)


#  CHARACTERS
class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)

    name = Column(String(100), unique=True)
    hair_color = Column(String(500), unique=True)
    eye_color = Column(String(500), unique=True)
    gender = Column(String(500), unique=True)
    birth_year = Column(String(500), unique=True)
    homeworld = Column(String(500), unique=True)
    height = Column(String(500), unique=True)

    user_id = Column(Integer, ForeignKey('user.id'))

class Characterfavourites(Base):
    __tablename__ = 'characterfavourites'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

#  PLANETS
class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)

    name = Column(String(100), unique=True)
    climate = Column(String(500), unique=True)
    diameter = Column(String(500), unique=True)
    gravity = Column(String(500), unique=True)
    residents = Column(String(500), unique=True)

    user_id = Column(Integer, ForeignKey('user.id'))

class Planetfavourites(Base):
    __tablename__ = 'planetfavourites'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))


# VEHICLES
class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)

    name = Column(String(100), unique=True)
    cargo_capacity = Column(String(500), unique=True)
    crew = Column(String(500), unique=True)
    length = Column(String(500), unique=True)
    model = Column(String(500), unique=True)
    nam = Column(String(500), unique=True)
    passengers = Column(String(500), unique=True)

    user_id = Column(Integer, ForeignKey('user.id'))

class Vehiclefavourites(Base):
    __tablename__ = 'vehiclefavourites'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
