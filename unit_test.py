from unittest import TestCase
"""
This is a possible interview coding question. Let's check the task,
implement our solution and then write tests for it:

Task
Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'

Constraint notes:
an input integer is always withing the range 1 to 100 inclusive
"""

from code_to_test_unit_test import red_or_blue, is_within_range



class TestRedOrBlueFunction(TestCase):

    def test_odd_numbers(self):
        expected = 'Red'
        result = red_or_blue(num=3)
        self.assertEqual(expected, result)

    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = red_or_blue(num=54)
        self.assertEqual(expected, result)
        # delete pass and complete this test function to test the number 54

    def test_range_6_to_20(self):
        expected = True
        result = is_within_range(21, 6, 20)
        self.assertEqual(expected, result)
        # delete pass and complete this test function to test the number 12