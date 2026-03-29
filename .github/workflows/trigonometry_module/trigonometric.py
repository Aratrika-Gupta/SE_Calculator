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
        return math.degrees(math.asin(float(x)))

    def acos(self, x):
        return math.degrees(math.acos(float(x)))

    def atan(self, x):
        return math.degrees(math.atan(float(x)))

    def sinh(self, x):
        return math.sinh(float(x))

    def cosh(self, x):
        return math.cosh(float(x))

    def tanh(self, x):
        return math.tanh(float(x))
    
#OK