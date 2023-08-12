#!/usr/bin/python3
""" this module defines the tests for state """
import unittest
import os
import models
from models.state import State
from datetime import datetime


class Test_State_instancing(unittest.TestCase):
    """ This class defines the instancing test cases """

    def test_1(self):
        self.assertEqual(State, type(State()))

    def test_2(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_3(self):
        first = State()
        second = State()
        self.assertNotEqual(first.id, second.id)

    def test_4(self):
        first = State(None)
        self.assertNotIn(None, first.__dict__.values())
