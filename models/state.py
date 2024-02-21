#!/usr/bin/python3
""" class for state """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, relationship
from models.city import City
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ class for state """

    __tablename__ = 'states'
    HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

    if HBNB_TYPE_STORAGE == "db":  # if db only
        cities = relationship("City", backref="state")
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ init State class"""
        super().__init__(*args, **kwargs)

    if HBNB_TYPE_STORAGE == "db":  # if db only
        @property
        def cities(self):
            """returns the list of City instances"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
