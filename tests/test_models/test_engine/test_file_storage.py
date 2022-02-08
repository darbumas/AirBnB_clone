#!/usr/bin/python3
'''Unittest for storage engine'''

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    '''Class to test FileStorage'''

    def test_attr(self):
        '''Test private attributes "file_path" & "objects"'''
        engine = FileStorage()
        obj, path = engine._FileStorage__objects, engine._FileStorage__file_path
        self.assertTrue(hasattr(engine, "_FileStorage__file_path"))
        self.assertTrue(hasattr(engine, "_FileStorage__objects"))
        self.assertIsInstance(obj, dict)
        self.assertIsInstance(path, str)

    def test_methods(self):
        '''Test for public methods'''
        engine = FileStorage()
        self.assertTrue(hasattr(engine, 'all'))
        self.assertTrue(hasattr(engine, 'new'))
        self.assertTrue(hasattr(engine, 'save'))
        self.assertTrue(hasattr(engine, 'reload'))

    def tests_save(self):
        '''Test dictionary saved from reload'''
        os.remove("file.json")
        model = BaseModel()
        model.save()
        storage.reload()
        new_model = storage.all()
        self.assertDictEqual(new_model["BaseModel." + model.id].to_dict(),
                             model.to_dict())

    def test_engines(self):
        '''Test if each instance is always different'''
        engine1 = FileStorage()
        engine2 = FileStorage()
        self.assertNotEqual(engine1, engine2)

    def test_instance(self):
        '''Test for instance'''
        engine = FileStorage()
        self.assertIsInstance(engine, FileStorage)

if __name__ == "__main__":
    unittest.main()
