#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    longitude = Column(Float)
    number_rooms = Column(Integer, default=0, nullable=False)
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False, )
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    description = Column(String(1024))
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)

    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
        reviews = relationship("Review", cascade="all, delete, \
                               delete-orphan",
                               backref="place")
    else:
        @property
        def reviews(self):
            """ returns the list of Review instances with place_id"""
            all_storage = models.storage.all()
            temp_list = []
            return_list = []
            for key in all_storage:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    temp_list.append(all_storage[key])
            for rev in all_storage:
                if (rev.place_id == self.id):
                    return_list.append(rev)
            return return_list

    @property
    def amenities(self):
        """ returns the list of Amenity instances"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """ adds an amenity id to the list"""
        if type(obj) is models.Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
