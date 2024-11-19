import unittest
from unittest.mock import patch
from calculator import calculator

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '10', '5'])
    @patch('builtins.print')
    def test_add(self, mock_print, mock_input):
        calculator()
        mock_print.assert_called_with('10.0 + 5.0 = 15.0')

    @patch('builtins.input', side_effect=['2', '10', '5'])
    @patch('builtins.print')
    def test_subtract(self, mock_print, mock_input):
        calculator()
        mock_print.assert_called_with('10.0 - 5.0 = 5.0')

    @patch('builtins.input', side_effect=['3', '10', '5'])
    @patch('builtins.print')
    def test_multiply(self, mock_print, mock_input):
        calculator()
        mock_print.assert_called_with('10.0 * 5.0 = 50.0')

    @patch('builtins.input', side_effect=['4', '10', '5'])
    @patch('builtins.print')
    def test_divide(self, mock_print, mock_input):
        calculator()
        mock_print.assert_called_with('10.0 / 5.0 = 2.0')

    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_invalid_input(self, mock_print, mock_input):
        calculator()
        mock_print.assert_called_with('Invalid input')

if __name__ == '__main__':
    unittest.main()