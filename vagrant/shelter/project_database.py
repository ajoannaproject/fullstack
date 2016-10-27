# begin config #

import os

import sys

import enum

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

####end config####

# begin class defs #

class Shelter(Base):

    __tablename__ = 'shelter'

    name = Column(String(80), nullable = False)

    address = Column(String(80))

    city = Column(String(80))

    state = Column(String(80))

    zipCode = Column(Integer)

    website = Column(String)

    id = Column(Integer, primary_key = True)

class Puppy(Base):

    __tablename__ = 'puppy'

    name = Column(String(80))

    id = Column(Integer, primary_key = True)

    dob = Column(String(8))

    class GenderEnum(enum.Enum):
        f = "female"
        m = "male"
        o = "other"

    gender = Table(
        'data', MetaData(),
        Column('value', Enum(GenderEnum))
        )

    weight = Column(Integer)

    shelter_id = Column(Integer, ForeignKey('shelter.id'))

    shelter = relationship(Shelter)

#### end class defs ####

# begin creating .db file and add classes to it #

engine = create_engine(
    'sqlite:///puppies.db')

Base.metadata.create_all(engine)

#### end creating .db file and add classes to it ####