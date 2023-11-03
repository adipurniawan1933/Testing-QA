import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
