#!/usr/bin/python3
"""
    FileStorage class serializes instances to a JSON file
    and deserializes JSONfile to instances
"""

import json
import os


class FileStorage:
    """
        Private Attributes:
            __file_path: string - path to the JSON file (ex: file.json)
            __objects: dictionary - empty but will store all objects
                    by <class name>.id (ex: to store a BaseModel object with
                    id=12121212, the key will be BaseModel.12121212)
        Public instance methods:
            all(self):  string - path to the JSON file (ex: file.json)
            new(self, obj): sets in __objects the obj with key
                            <obj class name>.id
            save(self): serializes __objects to the JSON file
                        (path: __file_path)
            reload(self): deserializes the JSON file to __objects
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
        class_name = obj.__class__.__name__
        id_obj = getattr(obj, 'id', None)

        if id_obj is not None:
            key = f"{class_name}.{id_obj}"
            self.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        dict_obj = {}
        for key, obj in self.__objects.items():
            dict_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(dict_obj, json_file);



    def reload(self):
        from ..base_model import BaseModel
        """
            deserializes the JSON file to __objects
            only if the JSON file (__file_path) exists
             otherwise, do nothing. If the file doesn’t exist,
             no exception should be raised)
        """
        if os.path.exists(self.__file_path) and\
                os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as file:
                dictionaries_obj = json.load(file)
                for key, obj in dictionaries_obj.items():
                    self.__objects[key] = BaseModel(**obj)

