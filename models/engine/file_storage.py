#!/usr/bin/python3
"""Module creates a class 'FileStorage' to serialize/deserialize simple python
data structures to/from JSON format."""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    '''cls to render instance serialization to a JSON file and deserialization
    from JSON file to instance'''

    classes = {"BaseModel": BaseModel, "User": User}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns a dictionary "__objects" with all the values stored'''
        return self.__objects

    def new(self, obj):
        '''method to set in __objects the obj w/ key: <obj class name>.id'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        my_dict = {}
        for key, val in self.__objects.items():
            my_dict[key] = val.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as js_file:
            json.dump(my_dict, js_file)

    def reload(self):
        '''deseiralizes the JSON file to __objects'''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as js_file:
                self.__objects = {}
                my_dict = json.load(js_file)
                for key, val in my_dict.items():
                    my_list = key.split(".")
                    my_obj = self.classes[my_list[0]]
                    self.__objects[key] = my_obj(**val)
        except:
            pass
