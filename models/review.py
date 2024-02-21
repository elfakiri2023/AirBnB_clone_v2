#!/usr/bin/python3
"""class for the users reviews in the database"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """class for the users reviews in the database"""
    __tablename__ = "reviews"

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
