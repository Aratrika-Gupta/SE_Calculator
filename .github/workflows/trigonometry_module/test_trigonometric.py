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
    
    #more test cases:
    def test_sin_zero(self):
        self.assertAlmostEqual(self.calc.evaluate("sin(0)"), 0.0, places=2)

    def test_cos_zero(self):
        self.assertAlmostEqual(self.calc.evaluate("cos(0)"), 1.0, places=2)

    def test_tan_zero(self):
        self.assertAlmostEqual(self.calc.evaluate("tan(0)"), 0.0, places=2)

    def test_asin_one(self):
        self.assertAlmostEqual(self.calc.evaluate("asin(1)"), 90.0, places=2)

    def test_acos_one(self):
        self.assertAlmostEqual(self.calc.evaluate("acos(1)"), 0.0, places=2)

    def test_expression_mix(self):
        self.assertAlmostEqual(self.calc.evaluate("5 + 2*cos(60)"), 6.0, places=2)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("sin()")

    def test_invalid_function(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("sinn(30)")

if __name__ == "__main__":
    unittest.main()