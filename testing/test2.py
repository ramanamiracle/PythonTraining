#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
ut_template.py: Unit test template
"""
import unittest


class MyTestClass(unittest.TestCase):

    # Run before ALL test methods in this class.
    @classmethod
    def setUpClass(cls):
        print('run setUpClass()')

    # Run after ALL test methods in this class.
    @classmethod
    def tearDownClass(cls):
        print('run tearDownClass()')

    # Run before EACH test method.
    def setUp(self):
        print('run setUp()')

    # Run after EACH test method.
    def tearDown(self):
        print('run tearDown()')

    # A test method
    def test_numbers_equal(self):
        print('run test_numbers_equal()')
        self.assertEqual(8, 8)

    # Another test method
    def test_numbers_not_equal(self):
        print('run test_numbers_not_equal()')
        self.assertNotEqual(8, -8)


# Run the test cases in this module
if __name__ == '__main__':
    unittest.main()