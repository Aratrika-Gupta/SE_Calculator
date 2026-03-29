import unittest
from calculator import Calculator

class TestTrigonometric(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_sin(self):
        self.assertAlmostEqual(self.calc.evaluate("sin(30)"), 0.5, places=2)

    def test_cos(self):
        self.assertAlmostEqual(self.calc.evaluate("cos(60)"), 0.5, places=2)

    def test_tan(self):
        self.assertAlmostEqual(self.calc.evaluate("tan(45)"), 1.0, places=2)

    def test_expression(self):
        self.assertAlmostEqual(self.calc.evaluate("2 + 3*sin(30)"), 3.5, places=2)

    def test_inverse(self):
        self.assertAlmostEqual(self.calc.evaluate("asin(0.5)"), 30, places=2)

    def test_hyperbolic(self):
        self.assertAlmostEqual(self.calc.evaluate("sinh(0)"), 0.0, places=2)

    def test_division_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            self.calc.evaluate("10/0")

    def test_invalid_expression(self):
        with self.assertRaises(InvalidExpressionError):
            self.calc.evaluate("2 + * 3")

    def test_asin_domain_error(self):
        with self.assertRaises(DomainError):
            self.calc.evaluate("asin(2)")

    def test_empty_expression(self):
        with self.assertRaises(InvalidExpressionError):
            self.calc.evaluate("")

    def test_non_string_expression(self):
        with self.assertRaises(InvalidExpressionError):
            self.calc.evaluate(123)

if __name__ == "__main__":
    unittest.main()