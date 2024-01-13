#!/usr/bin/python3
""" Test file for State class """
from models.engine.file_storage import FileStorage
from models.state import State
import unittest
from datetime import datetime
from time import sleep
import os
import shutil


class TestState(unittest.TestCase):
    """
        Test class for State class
    """
    back_up_path = "back_up.json"
    original_path = FileStorage._FileStorage__file_path

    def setUp(self) -> None:
        """
            setUp method to create a backup file for
            file.json
        """
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
        model = State()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertTrue(hasattr(model, 'name'))

        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """
            init with kwargs testing
        """
        model = State()
        model_dict = model.to_dict()
        new_model = State(**model_dict)

        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertIsInstance(model, State)
        self.assertIsInstance(new_model, State)

    def test_save_method(self):
        """
            save() method testing
        """
        model = State()
        initial_updated_at = model.updated_at
        sleep(0.1)
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
            to_dict() methos testing
        """
        model = State()
        model.name = "state"

        model_dict = model.to_dict()

        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('name', model_dict)

    def test_to_dict_values(self):
        """
            to_dict() methos testing
        """
        model = State()
        model.name = "state"

        model_dict = model.to_dict()

        model_created_at = datetime.fromisoformat(model_dict['created_at'])
        model_updated_at = datetime.fromisoformat(model_dict['updated_at'])

        self.assertEqual(model_dict['__class__'], 'State')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_created_at, model.created_at)
        self.assertEqual(model_updated_at, model.updated_at)
        self.assertEqual(model.name, model_dict['name'])

    def test_str_method(self):
        """
            __str__ method testing
        """
        model = State()
        expected_output = f"[{model.__class__.__name__}] \
({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)


if __name__ == '__main__':
    unittest.main()
