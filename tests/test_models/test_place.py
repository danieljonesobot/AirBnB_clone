#!/usr/bin/python3
""" this module tests the place class"""
from models.place import Place
import os
import unittest
import models
from datetime import datetime


class Test_place_instancing(unittest.TestCase):
    """ tis calss test the inistacning of the place class """

    def test_1(self):
        self.assertEqual(Place, type(Place()))

    def test_2(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_3(self):
        first = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(first))
        self.assertNotIn("name", first.__dict__)

    def test_4(self):
        first = Place()
        second = Place()
        self.assertNotEqual(first.id, second.id)
