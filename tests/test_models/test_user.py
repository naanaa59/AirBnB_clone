#!/usr/bin/python3
""" Test file for User class """

from models.user import User
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
from time import sleep
import os
import shutil


class TestUser(unittest.TestCase):
    """Unittest class for testing class User
    Test the following attributes
    - email = ""
    - password = ""
    - first_name = ""
    - last_name = ""
    """
    back_up_path = "back_up.json"
    original_path = FileStorage._FileStorage__file_path
    model = User()
    model.email = "test@gmail.com"
    model.password = "root"
    model.first_name = "my_first"
    model.last_name = "my_last"

    def setUp(self) -> None:
        """
            setUp method to create a backup file for
            file.json
        """
        model_dict = self.model.to_dict()
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

        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertTrue(hasattr(self.model, 'email'))
        self.assertTrue(hasattr(self.model, 'password'))
        self.assertTrue(hasattr(self.model, 'first_name'))
        self.assertTrue(hasattr(self.model, 'last_name'))
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """
            init with kwargs testing
        """
        model_dict = self.model.to_dict()
        new_model = User(**model_dict)

        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertIsInstance(self.model, User)
        self.assertIsInstance(new_model, User)

    def test_save_method(self):
        """
            save() method testing
        """

        initial_updated_at = self.model.updated_at
        sleep(0.1)
        self.model.save()
        self.assertNotEqual(self.model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
            to_dict() methos testing
        """
        model_dict = self.model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('email', model_dict)
        self.assertIn('password', model_dict)
        self.assertIn('first_name', model_dict)
        self.assertIn('last_name', model_dict)

    def test_to_dict_values(self):
        """
            to_dict() methos testing
        """
        model = User()
        model.email = "test@gmail.com"
        model.password = "root"
        model.first_name = "my_first"
        model.last_name = "my_last"
        model_dict = model.to_dict()
        model_created_at = datetime.fromisoformat(model_dict['created_at'])
        model_updated_at = datetime.fromisoformat(model_dict['updated_at'])

        self.assertEqual(model_dict['__class__'], 'User')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_created_at, model.created_at)
        self.assertEqual(model_updated_at, model.updated_at)
        self.assertEqual(model.password, model_dict['password'])
        self.assertEqual(model.email, model_dict['email'])
        self.assertEqual(model.first_name, model_dict['first_name'])
        self.assertEqual(model.last_name, model_dict['last_name'])

    def test_str_method(self):
        """
            __str__ method testing
        """
        model = User()
        expected_output = f"[{model.__class__.__name__}] \
({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)


if __name__ == '__main__':
    unittest.main()
