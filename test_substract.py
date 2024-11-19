import unittest
from substract import subtract

# FILE: test_substract.py


class TestSubtract(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -5), -5)

    def test_subtract_positive_and_negative(self):
        self.assertEqual(subtract(10, -5), 15)

    def test_subtract_zero_from_number(self):
        self.assertEqual(subtract(10, 0), 10)

    def test_subtract_number_from_zero(self):
        self.assertEqual(subtract(0, 10), -10)

if __name__ == '__main__':
    unittest.main()