#!/usr/bin/python3

""" Test file for Place class """
from models.engine.file_storage import FileStorage
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
import unittest
from datetime import datetime
from time import sleep
import os
import shutil


class TestPlace(unittest.TestCase):
    """
        Test class for Place class
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
        model = Place()
        cty = City()
        usr = User()
        am = Amenity()
        model.city_id = cty.id
        model.user_id = usr.id
        model.name = "a place"
        model.description = "some description"
        model.number_bathrooms = 4
        model.number_rooms = 4
        model.max_guest = 10
        model.price_by_night = 20
        model.latitude = 1.3
        model.longitude = 1.5
        model.amenity_ids = am.id

        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertTrue(hasattr(model, 'name'))
        self.assertTrue(hasattr(model, 'city_id'))
        self.assertTrue(hasattr(model, 'user_id'))
        self.assertTrue(hasattr(model, 'description'))
        self.assertTrue(hasattr(model, 'number_rooms'))
        self.assertTrue(hasattr(model, 'number_bathrooms'))
        self.assertTrue(hasattr(model, 'max_guest'))
        self.assertTrue(hasattr(model, 'price_by_night'))
        self.assertTrue(hasattr(model, 'latitude'))
        self.assertTrue(hasattr(model, 'longitude'))
        self.assertTrue(hasattr(model, 'amenity_ids'))

        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.city_id, str)
        self.assertIsInstance(model.user_id, str)
        self.assertIsInstance(model.name, str)
        self.assertIsInstance(model.description, str)
        self.assertIsInstance(model.number_bathrooms, int)
        self.assertIsInstance(model.number_rooms, int)
        self.assertIsInstance(model.max_guest, int)
        self.assertIsInstance(model.price_by_night, int)
        self.assertIsInstance(model.latitude, float)
        self.assertIsInstance(model.longitude, float)
        self.assertIsInstance(model.amenity_ids, str)

    def test_init_with_kwargs(self):
        """
            init with kwargs testing
        """
        model = Place()
        cty = City()
        usr = User()
        am = Amenity()
        model.city_id = cty.id
        model.user_id = usr.id
        model.name = "a place"
        model.description = "some description"
        model.number_bathrooms = 4
        model.number_rooms = 4
        model.max_guest = 10
        model.price_by_night = 20
        model.latitude = 1.3
        model.longitude = 1.5
        model.amenity_ids = am.id

        model_dict = model.to_dict()
        new_model = Place(**model_dict)

        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertEqual(model.city_id, new_model.city_id)
        self.assertEqual(model.user_id, new_model.user_id)
        self.assertEqual(model.name, new_model.name)
        self.assertEqual(model.number_bathrooms, new_model.number_bathrooms)
        self.assertEqual(model.number_rooms, new_model.number_bathrooms)
        self.assertEqual(model.max_guest, new_model.max_guest)
        self.assertEqual(model.price_by_night, new_model.price_by_night)
        self.assertEqual(model.latitude, new_model.latitude)
        self.assertEqual(model.longitude, new_model.longitude)
        self.assertEqual(model.amenity_ids, new_model.amenity_ids)

        self.assertIsInstance(model, Place)
        self.assertIsInstance(new_model, Place)

    def test_save_method(self):
        """
            save() method testing
        """
        model = Place()
        initial_updated_at = model.updated_at
        sleep(0.1)
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
            to_dict() methos testing
        """
        model = Place()
        cty = City()
        usr = User()
        am = Amenity()
        model.city_id = cty.id
        model.user_id = usr.id
        model.name = "a place"
        model.description = "some description"
        model.number_bathrooms = 4
        model.number_rooms = 4
        model.max_guest = 10
        model.price_by_night = 20
        model.latitude = 1.3
        model.longitude = 1.5
        model.amenity_ids = am.id

        model_dict = model.to_dict()

        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('city_id', model_dict)
        self.assertIn('user_id', model_dict)
        self.assertIn('description', model_dict)
        self.assertIn('number_bathrooms', model_dict)
        self.assertIn('number_rooms', model_dict)
        self.assertIn('max_guest', model_dict)
        self.assertIn('price_by_night', model_dict)
        self.assertIn('latitude', model_dict)
        self.assertIn('longitude', model_dict)
        self.assertIn('amenity_ids', model_dict)

    def test_to_dict_values(self):
        """
            to_dict() methos testing
        """
        model = Place()
        cty = City()
        usr = User()
        am = Amenity()
        model.city_id = cty.id
        model.user_id = usr.id
        model.name = "a place"
        model.description = "some description"
        model.number_bathrooms = 4
        model.number_rooms = 4
        model.max_guest = 10
        model.price_by_night = 20
        model.latitude = 1.3
        model.longitude = 1.5
        model.amenity_ids = am.id

        model_dict = model.to_dict()

        model_created_at = datetime.fromisoformat(model_dict['created_at'])
        model_updated_at = datetime.fromisoformat(model_dict['updated_at'])

        self.assertEqual(model_dict['__class__'], 'Place')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_created_at, model.created_at)
        self.assertEqual(model_updated_at, model.updated_at)
        self.assertEqual(model.user_id, model_dict['user_id'])
        self.assertEqual(model.city_id, model_dict['city_id'])
        self.assertEqual(model.description, model_dict['description'])
        self.assertEqual(
                model.number_bathrooms, model_dict['number_bathrooms'])
        self.assertEqual(model.number_rooms, model_dict['number_rooms'])
        self.assertEqual(model.max_guest, model_dict['max_guest'])
        self.assertEqual(model.latitude, model_dict['latitude'])
        self.assertEqual(model.longitude, model_dict['longitude'])
        self.assertEqual(model.amenity_ids, model_dict['amenity_ids'])

    def test_str_method(self):
        """
            __str__ method testing
        """
        model = Place()
        expected_output = f"[{model.__class__.__name__}] \
({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)
