#!/usr/bin/python3
'''Unittest for class ``Amenity``'''

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    '''Init class to test Amenity'''

    def test_class(self):
        '''Test for inheritance'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        '''Test for attributes'''
        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)

if __name__ == '__main__':
    unittest.main()
