#!/usr/bin/python3
''' Unittest for Base '''

import unittest
from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


class TestBase(unittest.TestCase):
    ''' The test base class '''

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1(self):
        """create an instance and check id."""

        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(32).id, 32)
        self.assertEqual(Base(2000).id, 2000)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-10).id, -10)
        self.assertEqual(Base().id, 3)

        b = Base()
        self.assertEqual(type(b), Base)
        self.assertTrue(isinstance(b, Base))
