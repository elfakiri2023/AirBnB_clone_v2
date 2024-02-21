#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class  for HBNB project"""
    
    __tablename__ = "states"
    
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref='state',
                          cascade="all, delete-orphan")