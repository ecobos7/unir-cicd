import unittest
import pytest

from app.calc import Calculator


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.multiply(2, 4))
        self.assertEqual(-4, self.calc.multiply(2, -2))
        self.assertEqual(6, self.calc.multiply(-2, -3))
        self.assertEqual(-6, self.calc.multiply(-2, 3))
        self.assertEqual(0, self.calc.multiply(2, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(0.125, self.calc.power(2, -3))
        self.assertEqual(-8, self.calc.power(-2, 3))
        self.assertEqual(-0.125, self.calc.power(-2, -3))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(1, self.calc.power(-2, 0))
        self.assertEqual(0, self.calc.power(0, 3))
        self.assertEqual(1, self.calc.power(0, 0))

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(5, self.calc.sqrt(25))

    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(3, self.calc.log10(1000))
    

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
 
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    def test_sqrt_method_fails_with_sqrt_of_negative(self):
        self.assertRaises(TypeError, self.calc.sqrt, -10)

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "2")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

    def test_log10_method_fails_with_log10_of_negative(self):
        self.assertRaises(TypeError, self.calc.log10, -10)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
