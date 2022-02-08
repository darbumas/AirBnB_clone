#!/usr/bin/python3
'''Unittest for class ``Amenity``'''

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    '''Init class to test Amenity'''

    def test_class(self):
        '''Test for inheritance'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        '''Test for attributes'''
        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Place.city_id, str)
            self.assertIsInstance(Place.user_id, str)
            self.assertIsInstance(Place.name, str)
            self.assertIsInstance(Place.description, str)
            self.assertIsInstance(Place.number_rooms, int)
            self.assertIsInstance(Place.number_bathrooms, int)
            self.assertIsInstance(Place.max_guest, int)
            self.assertIsInstance(Place.price_by_night, int)
            self.assertIsInstance(Place.latitude, float)
            self.assertIsInstance(Place.longitude, float)
            self.assertIsInstance(Place.amenity_ids, list)

if __name__ == "__main__":
    unittest.main()
