#!/usr/bin/python3
"""class for the users table in the database"""
from models.base_model import BaseModel
from models.base_model import Base
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """class for the users table in the database"""

    __tablename__ = "users"

    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    email = Column(String(128), nullable=False)
    last_name = Column(String(128))
    places = relationship("Place",
                          cascade='all, delete, delete-orphan',
                          backref='user')
    reviews = relationship("Review",
                           cascade='all, delete, delete-orphan',
                           backref='user')
