#!/usr/bin/python3
""" this module defines the tests for amenity """
import unittest
import os
import models
from models.amenity import Amenity
from datetime import datetime


class Test_Amenity_instancing(unittest.TestCase):
    """ This class defines the instancing test cases """

    def test_1(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_2(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_3(self):
        first = Amenity()
        second = Amenity()
        self.assertNotEqual(first.id, second.id)

    def test_4(self):
        first = Amenity(None)
        self.assertNotIn(None, first.__dict__.values())
