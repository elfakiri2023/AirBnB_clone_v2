#!/usr/bin/python3
"""Place class for the database"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
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
    """Place class for the database"""
    __tablename__ = "places"

    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    name = Column(String(128), nullable=False)
    longitude = Column(Float)
    description = Column(String(1024))
    amenity_ids = []

    HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

    #  If the storage type is file, the relationship between Place and Review
    if HBNB_TYPE_STORAGE == "db":
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

    else:
        @property
        def amenities(self):
            """ list of all amenities ids """
            return self.amenity_ids

        @property
        def reviews(self):
            """ list of all reviews"""
            temp_list = []
            final_list = []
            all_storage = models.storage.all()
            for key in all_storage:
                review_arr = shlex.split(key.replace('.', ' '))
                if ('Review' == review_arr[0]):
                    temp_list.append(all_storage[key])
            for elem in temp_list:
                if (self.id == elem.place_id): # if place_id matches
                    final_list.append(elem)
            return (final_list)

        @amenities.setter
        def amenities(self, obj=None):
            """ method to add amenities to the list"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
