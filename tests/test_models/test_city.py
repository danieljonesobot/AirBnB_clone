#!/usr/bin/python3
""" the test file for city class """

import os
from datetime import datetime
import models
from time import sleep
from models.city import City
import unittest


class Test_City_Instancing(unittest.TestCase):
    """class for testing instancing of the class city"""

    def test_1(self):
        self.assertEqual(City, type(City()))

    def test_2(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_3(self):
        first = City()
        second = City()
        self.assertNotEqual(first.id, second.id)

    def test_4(self):
        first = City(None)
        self.assertNotIn(None, first.__dict__.values())
