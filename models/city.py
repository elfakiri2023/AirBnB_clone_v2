#!/usr/bin/python3
"""class for the users cities in the database"""

from models.base_model import BaseModel
from models.base_model import Base
# from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """class for the users cities in the database"""

    __tablename__ = "cities"

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete, delete-orphan')
