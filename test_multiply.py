import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-10, -5), 50)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply(10, -5), -50)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_multiply_zero_by_number(self):
        self.assertEqual(multiply(0, 10), 0)

if __name__ == '__main__':
    unittest.main()