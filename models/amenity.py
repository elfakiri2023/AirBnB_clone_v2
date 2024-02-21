#!/usr/bin/python3
""" Amenity class for the database """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ Amenity class for the database """
    __tablename__ = "amenities"
    place_amenities = relationship("Place", secondary=place_amenity)
    name = Column(String(128), nullable=False)
