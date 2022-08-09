import math
# from math import hypot
from functools import total_ordering


@total_ordering
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Operation only supported between instances of vector")

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if not type(other) == int and not type(other) == float:
            raise TypeError("Operation only supported for a numeric scalar")

        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        # return self.__mul__(other)
        return self * other

    def __abs__(self):  # -> abs()
        # return math.hypot(self.x, self.y, self.z)
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __le__(self, other):
        if not isinstance(other, Vector):
            return TypeError("must be a vector")

        return abs(self) < abs(other)

    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, item):
        if type(item) == str and item.lower() in ['x', 'y', 'z']:
            return eval(f"self.{item.lower()}")
        else:
            return NotImplemented
