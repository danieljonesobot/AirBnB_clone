#!/usr/bin/python3
""" this module is the unittest for the basemodel class .

classes for unittest:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestInit(unittest.TestCase):
    """testing the init method ."""

    def test_1_missing_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))


    def test_3(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_4(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_5(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_6(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_7_create_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_8_updated_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)

    def test_10(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class Testsave(unittest.TestCase):
    """This unittest to test the save method."""

    @classmethod
    def settingFile(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def removingFile(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_1(self):
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        self.assertLess(first_updated_at, base.updated_at)

    def test_2(self):
        base = BaseModel()
        sleep(0.05)
        first_t = base.updated_at
        base.save()
        second_t = base.updated_at
        self.assertLess(first_t, second_t)
        sleep(0.05)
        base.save()
        self.assertLess(second_t, base.updated_at)

    def test_3(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

class TestDict(unittest.TestCase):
    """Unittest to test the dict method ."""

    def test_1(self):
        self.assertTrue(dict, type(BaseModel().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
