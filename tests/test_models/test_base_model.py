#!/usr/bin/python3
"""
A unittest for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import time


class Test_BaseModel_Class(unittest.TestCase):
    """Unittest class for testing class BaseModel
    Test the following attributes
"""
    def setUp(self):
        """setUp method"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """tearDown method"""
        del self.b1
        del self.b2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_BaseModel_id(self):
        """Test BaseModel instance id"""
        self.assertNotEqual(self.b1.id, self.b2.id)

    # ***************************************************************
    # *********************************************************
    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_initial_values(self):
        """Test initial values for BaseModel class attributes"""

    def test_BaseModel_inherits_BaseModel(self):
        """Test if BaseModel inherits from BaseModel"""
        self.assertIsInstance(self.b1, BaseModel)

    def test_BaseModel_type(self):
        """Test if BaseModel instance is of the same type"""
        self.assertEqual(type(self.b1), BaseModel)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.b1.__class__.__name__}.{self.b1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.b2.__class__.__name__}.{self.b2.id}"
        self.assertTrue(search_key in storage.all().keys())

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.b1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('id', dict_c1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.b1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('created_at', dict_c1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.b1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('updated_at', dict_c1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.b1.to_dict()
        self.assertEqual(self.b1.__class__.__name__, dict_c1["__class__"])

    def test_str_(self):
        """Test __str__ method from BaseModel"""
        cls_rp = str(self.b1)
        format = "[{}] ({}) {}".format(self.b1.__class__.__name__,
                                       self.b1.id, self.b1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_c1 = self.b1.to_dict()
        instance = BaseModel(**dict_c1)
        self.assertIsNot(self.b1, instance)
        self.assertEqual(str(self.b1), str(instance))
        self.assertFalse(instance is self.b1)

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.b1.updated_at
        time.sleep(0.1)
        self.b1.save()
        updated_new = self.b1.updated_at
        self.assertNotEqual(update_old, updated_new)


if __name__ == "__main__":
    unittest.main()
