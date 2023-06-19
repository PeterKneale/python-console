import unittest
from src.calculator import add_numbers


class TestCalculator(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add_numbers(-1, -2)
        self.assertEqual(result, -3)
