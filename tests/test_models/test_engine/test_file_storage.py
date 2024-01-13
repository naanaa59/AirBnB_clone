#!/usr/bin/env python3
"""
    This is unittest for FileStorage class
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage
import unittest
import os
import json
import shutil


class TestFileStorage(unittest.TestCase):
    """
        Test class for FileStorage class
    """
    back_up_path = "back_up.json"
    original_path = FileStorage._FileStorage__file_path

    def setUp(self) -> None:
        if os.path.exists(FileStorage._FileStorage__file_path):
            shutil.copy(self.original_path, self.back_up_path)

    def tearDown(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        if os.path.exists(self.back_up_path):
            shutil.move(self.back_up_path, self.original_path)

    def test_all_method(self):
        """
            all method testing to returns __objects
        """
        result = storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method(self):
        """
            new() method testing for adding new object to __objects
        """
        bm = BaseModel()
        storage.new(bm)
        self.assertIn("BaseModel." + bm.id, storage.all().keys())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_save_method(self):
        """
            save() method testing if called
        """
        bm = BaseModel()
        usr = User()
        cty = City()
        pl = Place()
        am = Amenity()
        st = State()
        rv = Review()

        storage.save()
        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", 'r') as json_file:
            data = json.load(json_file)

        self.assertIn("BaseModel." + bm.id, data)
        self.assertIn("User." + usr.id, data)
        self.assertIn("City." + cty.id, data)
        self.assertIn("Place." + pl.id, data)
        self.assertIn("Amenity." + am.id, data)
        self.assertIn("State." + st.id, data)
        self.assertIn("Review." + rv.id, data)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method(self):
        bm = BaseModel()
        usr = User()
        cty = City()
        pl = Place()
        am = Amenity()
        st = State()
        rv = Review()

        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objects)
        self.assertIn("User." + usr.id, objects)
        self.assertIn("Place." + pl.id, objects)
        self.assertIn("City." + cty.id, objects)
        self.assertIn("State." + st.id, objects)
        self.assertIn("Amenity." + am.id, objects)
        self.assertIn("Review." + rv.id, objects)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()
