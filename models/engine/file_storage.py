#!/usr/bin/python3
"""This module manages the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets __objects to include obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Loads objects from JSON file (path: __file_path)"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
