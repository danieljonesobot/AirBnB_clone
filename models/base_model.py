import models
#!/usr/bin/python3
""" This this the base model that defines all common attributes/methods for the other classes:
"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ this is the base model class
    """
    
    def __init__(self):
        """this is the constructor method
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """ to print the str representation of the base model """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ this method to update the updated_at 
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """ converts to dictionary format
        """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.updated_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
