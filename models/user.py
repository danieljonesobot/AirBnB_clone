#!/usr/bin/python3

"""this module defines the class called User which inherits from
parent class BaseModel
"""

from base_model import BaseModel


class User(BaseModel):
    """constructor"""
    def __init__(self):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
