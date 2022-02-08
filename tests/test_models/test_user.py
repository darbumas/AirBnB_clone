#!/usr/bin/python3
'''Unittest for class ``User``'''

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    '''Test implementation of class ``User``'''

    def test_class(self):
        '''Test User is subclass of BaseModel'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

    def test_attr(self):
        '''Test User's attributes'''
        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)

if __name__ == '__main__':
    unittest.main()
