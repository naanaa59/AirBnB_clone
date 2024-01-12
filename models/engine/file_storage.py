#!/usr/bin/python3

"""
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os

class FileStorage:
    """
    attributes:
        __file_path: string - path to the JSON file
    (ex: file.json)
        __objects:  dictionary - empty but will store
    all objects by <class name>.id (ex: to store a BaseModel
    object with id=12121212, the key
    will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        serialized_objects = {}

        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open (self.__file_path, "w") as file:
            file.write(json.dumps(serialized_objects))

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        """
            deserializes the JSON file to __objects
            only if the JSON file (__file_path) exists
             otherwise, do nothing. If the file doesn’t exist,
             no exception should be raised)
        """
        classes = {
            'BaseModel': BaseModel, 'User': User,
            'State': State, 'Place': Place, 'City': City,
            'Amenity': Amenity, 'Review': Review}

        if os.path.exists(self.__file_path) and\
                os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as file:
                dictionaries_obj = json.load(file)
                for key, obj in dictionaries_obj.items():
                    class_name, instance_id = key.split('.')
                    self.__objects[key] = classes[key.split('.')[0]](**obj)
