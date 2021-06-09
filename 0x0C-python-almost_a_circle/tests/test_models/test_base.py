#!/usr/bin/python3
''' Unittest for Base '''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' The test base class '''

    def setUp(self):
        ''' setup def '''

        Base._Base__nb_objects = 0

    def test_1(self):
        """create an instance and check id."""

        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(24)
        self.assertEqual(b2.id, 24)
        b3 = Base(1024)
        self.assertEqual(b3.id, 1024)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)
    
    def test_1_2(self):
        ''' fill test '''

        b5 = Base(-10)
        self.assertEqual(b5.id, -10)
        b6 = Base(4)
        self.assertEqual(b6.id, 4)
        b7 = Base()
        self.assertEqual(b7.id, 3)

    def test_1_3(self):
        ''' aaaaaaaaaaaaaa '''

        b7 = Base()
        self.assertEqual(type(b7), Base)
        self.assertTrue(isinstance(b7, Base))

if __name__ == '__main__':
    unittest.main()
