#this is our "configuration:"
import os

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

##an instance of a declarative_base, called Base
Base = declarative_base()
####above this line is the beginning config code ####



class Restaurant(Base):

    __tablename__ = 'restaurant'

    name = Column(
        String(80), nullable = False)

    id = Column(
        Integer, primary_key = True)

class MenuItem(Base):

    __tablename__ = 'menuitem'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(
        Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

#####insert at end of file#####

#create instance of create_engine class and point to
#the database we will use
#since we are using sqlite, create_engine will create a new
#file we can use similarly to a more robust database
#like mysql or postgres
engine = create_engine(
'sqlite:///restaurantmenu.db')

#goes into database and adds the classes we will soon
#create as new tables in our database
Base.metadata.create_all(engine)



# copied from lesson, as reference for correctness

# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine

# Base = declarative_base()


# class Restaurant(Base):
#     __tablename__ = 'restaurant'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)


# class MenuItem(Base):
#     __tablename__ = 'menu_item'

#     name = Column(String(80), nullable=False)
#     id = Column(Integer, primary_key=True)
#     description = Column(String(250))
#     price = Column(String(8))
#     course = Column(String(250))
#     restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
#     restaurant = relationship(Restaurant)


# engine = create_engine('sqlite:///restaurantmenu.db')


# Base.metadata.create_all(engine)
