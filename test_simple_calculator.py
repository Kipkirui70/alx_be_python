import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for add ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Tests for subtract ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)

    # --- Tests for multiply ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiplication_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    # --- Tests for divide ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_division_result_decimal(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

if __name__ == "__main__":
    unittest.main()
