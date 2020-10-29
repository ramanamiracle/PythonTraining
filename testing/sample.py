#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
unittest_eg1.py: Unit test example
"""
import unittest


# Define a function to be unit-tested
def my_sum(a, b):
    """Return a + b"""
    return a + b


# Define a test case, which consists of a set of test methods.
class TestMySum(unittest.TestCase):  # subclass of TestCase
    def test_positive_inputs(self):
        result = my_sum(8, 80)
        self.assertEqual(result, 88)

    def test_negative_inputs(self):
        result = my_sum(-9, -90)
        self.assertEqual(result, -99)

    def test_mixed_inputs(self):
        result = my_sum(8, -9)
        self.assertEqual(result, -1)

    def test_zero_inputs(self):
        result = my_sum(0, 0)
        self.assertEqual(result, 0)


# Run the test cases in this module
if __name__ == '__main__':
    unittest.main()