#!/usr/bin/python3
""" This this the base model that defines
    all common attributes/methods for the other classes:
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ this is the base model class
    """

    def __init__(self, *args, **kwargs):
        """this is the constructor method
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    form = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, form))
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ to print the str representation of the base model """
        sid = self.id
        sldic = self.__dict__
        return "[{}] ({}) {}".format(self.__class__.__name__, sid, sldic)

    def save(self):
        """ this method to update the updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ converts to dictionary format
        """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.updated_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
