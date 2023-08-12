#!/usr/bin/python3
""" this module defines the tests for review """
import unittest
import os
import models
from models.review import Review
from datetime import datetime


class Test_Review_instancing(unittest.TestCase):
    """ This class defines the instancing test cases """

    def test_1(self):
        self.assertEqual(Review, type(Review()))

    def test_2(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_3(self):
        first = Review()
        second = Review()
        self.assertNotEqual(first.id, second.id)

    def test_4(self):
        first = Review(None)
        self.assertNotIn(None, first.__dict__.values())
