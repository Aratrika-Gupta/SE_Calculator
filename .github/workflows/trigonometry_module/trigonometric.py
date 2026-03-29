import math

class Trigonometric:

    def to_radians(self, x):
        return math.radians(float(x))

    def sin(self, x):
        return math.sin(self.to_radians(x))

    def cos(self, x):
        return math.cos(self.to_radians(x))

    def tan(self, x):
        return math.tan(self.to_radians(x))

    def asin(self, x):
        x = float(x)
        if x < -1 or x > 1:
            raise ValueError("asin domain is [-1,1]")
        return math.degrees(math.asin(x))

    def acos(self, x):
        x = float(x)
        if x < -1 or x > 1:
            raise ValueError("acos domain is [-1,1]")
        return math.degrees(math.acos(x))

    def atan(self, x):
        return math.degrees(math.atan(float(x)))

    def sinh(self, x):
        return math.sinh(float(x))

    def cosh(self, x):
        return math.cosh(float(x))

    def tanh(self, x):
        return math.tanh(float(x))