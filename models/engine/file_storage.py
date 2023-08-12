#!/usr/bin/python3
""" this module serializes from and to json format
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    """ this class stores the json to a file path
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary
        """
        return self.__objects

    def new(self, obj):
        """ sets in objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes object and sves to file
        """
        obj_ser = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_ser, f)

    def reload(self):
        """ relaod json from file and transforms it to dict
        """
        try:
            with open(self.__file_path, 'r') as f:
                to_dict = json.load(f)
                for key, value in to_dict.items():
                    class_name = value['__class__']
                    instance = globals()[class_name](**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
