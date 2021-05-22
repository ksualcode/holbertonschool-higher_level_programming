#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_max8(self):
      self.assertEqual(max_integer([3, 4, 8]), 8)

    def test_max_asd(self):
      self.assertEqual(max_integer("asd"), "s")

    def test_max_num(self):
      with self.assertRaisesRegex(TypeError, "object of type 'int' has no len()"):
          max_integer(8)

    def test_max_boolean(self):
      with self.assertRaisesRegex(TypeError, "object of type 'bool' has no len()"):
          max_integer(True)

if __name__ == '__main__':
    unittest.main()
