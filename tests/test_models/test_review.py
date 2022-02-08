#!/usr/bin/python3
'''Unittest for class ``State``'''

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    '''Init class to test State'''

    def test_class(self):
        '''Test to inheritance of class'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        '''Test for attributes'''
        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)

if __name__ == '__main__':
    unittest.main()
