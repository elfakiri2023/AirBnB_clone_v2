#!/usr/bin/python3
"""class for the users places in the database"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from models.base_model import BaseModel
from models.base_model import Base
from models.user import User


class Place(BaseModel, Base):
    """class for the places reviews in the database"""

    __tablename__ = "places"

    number_rooms = Column(Integer, default=0, nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    longitude = Column(Float, nullable=False)
