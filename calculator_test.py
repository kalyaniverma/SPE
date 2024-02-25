import unittest
from unittest.mock import patch
import calculator_main as calculator

class TestScientificCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(4), 2.0, delta=0.0001)
        self.assertAlmostEqual(calculator.square_root(9), 3.0, delta=0.0001)

    def test_factorial(self):
        self.assertEqual(calculator.factorial(0), 1)
        self.assertEqual(calculator.factorial(5), 120)

    def test_natural_logarithm(self):
        self.assertAlmostEqual(calculator.natural_logarithm(1), 0.0, delta=0.0001)
        self.assertAlmostEqual(calculator.natural_logarithm(2.71828), 1.0, delta=0.0001)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)

if __name__ == '__main__':
    unittest.main()
