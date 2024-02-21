#!/usr/bin/python3
""" Amenity class for the database """
from models.base_model import BaseModel
from models.base_model import Base
from models.place import place_amenity
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """ Amenity class for the database """
    __tablename__ = "amenities"
    place_amenities = relationship("Place", secondary=place_amenity)
    name = Column(String(128), nullable=False)
