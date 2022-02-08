#!/usr/bin/python3
'''Unittest for class ``City``'''

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''Init class to test City'''

    def test_class(self):
        '''Test for inheritance'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        '''Test for attributes'''
        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)

if __name__ == '__main__':
    unittest.main()
