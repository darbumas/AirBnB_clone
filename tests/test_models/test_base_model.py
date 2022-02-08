#!/usr/bin/python3
"""Unittest for module [models/base_model.py]"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''class to initiate testing'''

    def test_an_instance(self):
        '''test for an instance of ``BaseModel``'''
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id_set(self):
        '''test to see if attribute "id" is correctly being set'''
        my_model = BaseModel()
        self.assertTrue(my_model.id, my_model.id)

    def test_id_unique(self):
        '''test to see if "id" is unique for each instance'''
        zero_model = BaseModel()
        one_model = BaseModel()
        two_model = BaseModel()
        self.assertNotEqual(zero_model.id, one_model.id)
        self.assertNotEqual(zero_model.id, two_model.id)
        self.assertNotEqual(one_model.id, two_model.id)

    def test_str(self):
        '''test the __str__() method'''
        my_model = BaseModel()
        official_str = str(my_model)
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(official_str, expected_str)

    def test_save(self):
        '''test the instance method "save(self)" to check if attribute
        "updated_at" is being set correctly each time'''
        my_model = BaseModel()
        at_creation_time = my_model.updated_at
        my_model.save()
        at_save_time = my_model.updated_at
        self.assertNotEqual(at_creation_time, at_save_time)

    def test_to_dict(self):
        '''test the instance method "to_dict(self)" returns a dictionary and
        if keys are attributes: created_at, updated_at -> their values are
        string objects in ISO format'''
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIsInstance(my_dict, dict)
        for key, val in my_dict.items():
            flag = False
            if my_dict['__class__'] == 'BaseModel':
                flag = True
            self.assertFalse(flag is False)
        for key, val in my_dict.items():
            if key == 'created_at':
                self.assertIsInstance(val, str)
            if key == 'updated_at':
                self.assertIsInstance(val, str)

    def test_instance_from_dict(self):
        '''test creating an instance from a dictionary'''
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        new_model = BaseModel(**my_dict)
        new_model_dict = new_model.to_dict()
        self.assertIsInstance(new_model, BaseModel)
        self.assertIsInstance(new_model_dict, dict)
        self.assertFalse(new_model is my_model)
        self.assertTrue(new_model.id == my_model.id)

if __name__ == '__main__':
    unittest.main()
