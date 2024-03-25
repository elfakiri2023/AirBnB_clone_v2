#!/usr/bin/python3
"""The class for the database storage"""

import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    """The class for the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Connect to the database and create a session"""
        MYSQL_USER = getenv('HBNB_MYSQL_USER')
        MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            MYSQL_USER,
            MYSQL_PWD,
            MYSQL_HOST,
            MYSQL_DB))

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """new object to the current db"""
        self.__session.add(obj)

    def all(self, cls=None):
        """get all objects of a class or all objects"""
        new_dict = {}
        classes = {
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }

        for oneClass in classes:
            if cls is None or cls is classes[oneClass] or cls is oneClass:
                objs = self.__session.query(classes[oneClass]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def close(self):
        """close the session"""
        self.__session.remove()

    def reload(self):
        """create all tables in the databas"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        sess = scoped_session(session_maker)
        self.__session = sess

    def save(self):
        """save all changes of the current db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current db"""
        if obj is not None:
            self.__session.delete(obj)
