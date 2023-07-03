### Write 5 unit tests, including 1 that checks for a custom exception ###

from unittest import TestCase

from shop import buy_toy
class TestBuyToy(TestCase):

    def test_can_afford_cloudmobile(self):
        expected = 'Here’s your Cloudmobile!'
        result = buy_toy(customer_wallet=15, chosen_toy='Cloudmobile')
        self.assertEqual(expected, result)

    def test_can_afford_magic_roundabout(self):
        expected = 'Here’s your Magic Roundabout!'
        result = buy_toy(customer_wallet=95, chosen_toy='Magic Roundabout')
        self.assertEqual(expected, result)

    def test_cannot_afford_vent_doll(self):
        expected = True
        result = buy_toy(customer_wallet=100, chosen_toy='Ventriloquist Doll')
        self.assertNotEqual(expected, result)

    def test_exit_statement(self):
        expected = 'I\'m sorry we didn\'t have anything for you today'
        result = buy_toy(customer_wallet=100, chosen_toy='Exit')
        self.assertEqual(expected,result)

    def test_custom_exception(self):
        with self.assertRaises(Exception):
            buy_toy()

if __name__== '__main__':
    unittest.main()

### Framework we were given to help write the tests ###
# from unittest import TestCase
#
# Task
# Given an integer x perform the following conditional actions:
#
# If x is odd, return 'Red'
# If x is even and in the inclusive range of 2 to 5, return 'Blue'
# If x is even and in the inclusive range of 6 to 20, return 'Red'
# If x is even and greater than 20, return 'Blue'
#
# Constraint notes:
# an input integer is always within the range 1 to 100 inclusive
# """
#
# from code_to_test_unit_test import red_or_blue, is_within_range
#
#
# class TestRedOrBlueFunction(TestCase):
#
#     def test_odd_numbers(self):
#         expected = 'Red'
#         result = red_or_blue(num=3)
#         self.assertEqual(expected, result)
#
#     def test_even_greater_than_twenty(self):
#         expected = 'Blue'
#         result = red_or_blue(num=54)
#         self.assertEqual(expected, result)
#
#     def test_range_6_to_20(self):
#         expected = True
#         result = is_within_range(21, 6, 20)
#         self.assertEqual(expected, result)
