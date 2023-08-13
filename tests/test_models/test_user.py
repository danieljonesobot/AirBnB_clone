#!/usr/bin/python3
""" this module contains the test methods and clases for the User model

Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import unittest
from models.user import User
import os
import models
from datetime import datetime
from time import sleep


class TestInstantiation(unittest.TestCase):
    """ This class hodls the unitest for instance of a class."""

    def test_1_o_(self):
        self.assertEqual(User, type(User()))

    def test_2_o_(self):
        self.assertIn(User(), models.storage.all().values())

    def test_3_o_(self):
        self.assertEqual(str, type(User().id))

    def test_4_o_(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_5_o_(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_6_o_(self):
        self.assertEqual(str, type(User.email))

    def test_7_o_(self):
        self.assertEqual(str, type(User.password))

    def test_8_o_(self):
        self.assertEqual(str, type(User.first_name))

    def test_9_o_(self):
        self.assertEqual(str, type(User.last_name))

    def test_10_o_(self):
        person1_o_ = User()
        person2_o_ = User()
        self.assertNotEqual(person1_o_.id, person2_o_.id)

    def test_11_o_(self):
        person1_o_ = User()
        sleep(0.2)
        person2_o_ = User()
        self.assertLess(person1_o_.created_at, person2_o_.created_at)

    def test_12_o_(self):
        person1_o_ = User()
        sleep(0.2)
        person2_o_ = User()
        self.assertLess(person1_o_.updated_at, person2_o_.updated_at)

    def test_13_o_(self):
        person_o_ = User(None)
        self.assertNotIn(None, person_o_.__dict__.values())

    def test_14_o_(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestSave(unittest.TestCase):
    """class to test the save method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_1_o_(self):
        person_o_ = User()
        sleep(0.2)
        initial_updated_at_o_ = person_o_.updated_at
        person_o_.save()
        self.assertLess(initial_updated_at_o_, person_o_.updated_at)

    def test_2_o_(self):
        person_o_ = User()
        sleep(0.2)
        first_updated_at_o_ = person_o_.updated_at
        person_o_.save()
        second_updated_at_o_ = person_o_.updated_at
        self.assertLess(first_updated_at_o_, second_updated_at_o_)
        sleep(0.2)
        person_o_.save()
        self.assertLess(second_updated_at_o_, person_o_.updated_at)

    def test_3_o_(self):
        person_o_ = User()
        with self.assertRaises(TypeError):
            person_o_.save(None)

    def test_4_o_(self):
        person_o_ = User()
        person_o_.save()
        person_id_o_ = "User." + person_o_.id
        with open("file.json", "r") as f:
            self.assertIn(person_id_o_, f.read())


class TestToDict(unittest.TestCase):
    """this class tests to_dict method."""

    def test_1_o_(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_2_o_(self):
        person_o_ = User()
        self.assertIn("id", person_o_.to_dict())
        self.assertIn("created_at", person_o_.to_dict())
        self.assertIn("updated_at", person_o_.to_dict())
        self.assertIn("__class__", person_o_.to_dict())

    def test_3_o_(self):
        person_o_ = User()
        person_o_.extra_name = "Smith"
        person_o_.additional_number = 123
        self.assertEqual("Smith", person_o_.extra_name)
        self.assertIn("additional_number", person_o_.to_dict())

    def test_4_o_(self):
        person_o_ = User()
        person_dict_o_ = person_o_.to_dict()
        self.assertEqual(str, type(person_dict_o_["id"]))
        self.assertEqual(str, type(person_dict_o_["created_at"]))
        self.assertEqual(str, type(person_dict_o_["updated_at"]))

    def test_5_o_(self):
        current_datetime_o_ = datetime.today()
        person_o_ = User()
        person_o_.id = "789012"
        person_o_.created_at = person_o_.updated_at = current_datetime_o_
        expected_dict_o_ = {
            'id': '789012',
            '__class__': 'User',
            'created_at': current_datetime_o_.isoformat(),
            'updated_at': current_datetime_o_.isoformat(),
        }
        self.assertDictEqual(person_o_.to_dict(), expected_dict_o_)

    def test_6_o_(self):
        person_o_ = User()
        self.assertNotEqual(person_o_.to_dict(), person_o_.__dict__)

    def test_7_o_(self):
        person_o_ = User()
        with self.assertRaises(TypeError):
            person_o_.to_dict(None)


if __name__ == "__main__":
    unittest.main()
