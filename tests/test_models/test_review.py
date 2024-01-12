#!/usr/bin/env python3
""" Test file for Review class """
from models.engine.file_storage import FileStorage
from models.review import Review
from models.place import Place
from models.user import User
import unittest
from datetime import datetime
from time import sleep
import os
import shutil

class TestReview(unittest.TestCase):
    """
        Test class for Review class
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

    def test_init(self):
        """
            __init__ method testing
        """
        model = Review()
        usr = User()
        plc = Place()
        model.place_id = plc.id
        model.user_id = usr.id
        model.text = "some text"

        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertTrue(hasattr(model, 'place_id'))
        self.assertTrue(hasattr(model, 'user_id'))
        self.assertTrue(hasattr(model, 'text'))

        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.place_id, str)
        self.assertIsInstance(model.user_id, str)
        self.assertIsInstance(model.text, str)

    def test_init_with_kwargs(self):
        """
            init with kwargs testing
        """
        model = Review()
        model_dict = model.to_dict()
        new_model = Review(**model_dict)

        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertIsInstance(model, Review)
        self.assertIsInstance(new_model, Review)

    def test_save_method(self):
        """
            save() method testing
        """
        model = Review()
        initial_updated_at = model.updated_at
        sleep(0.1)
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
            to_dict() methos testing
        """
        model = Review()
        usr = User()
        plc = Place()
        model.place_id = plc.id
        model.user_id = usr.id
        model.text = "some text"

        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('place_id', model_dict)
        self.assertIn('user_id', model_dict)
        self.assertIn('text', model_dict)

    def test_to_dict_values(self):
        """
            to_dict() methos testing
        """
        model = Review()
        usr = User()
        plc = Place()
        model.place_id = plc.id
        model.user_id = usr.id
        model.text = "some text"

        model_dict = model.to_dict()

        model_created_at = datetime.fromisoformat(model_dict['created_at'])
        model_updated_at = datetime.fromisoformat(model_dict['updated_at'])
    
        self.assertEqual(model_dict['__class__'], 'Review')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_created_at, model.created_at)
        self.assertEqual(model_updated_at, model.updated_at)
        self.assertEqual(model_dict['place_id'], model.place_id)
        self.assertEqual(model_dict['user_id'], model.user_id)
        self.assertEqual(model_dict['text'], model.text)

    def test_str_method(self):
        """
            __str__ method testing
        """
        model = Review()
        expected_output = f"[{model.__class__.__name__}] \
({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)


if __name__ == '__main__':
    unittest.main()
