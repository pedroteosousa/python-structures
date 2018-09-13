"""This file hosts implementations of various geometry data structures."""

from math import sqrt

class Point(object):
    """This class represents a point in 2D space."""

    @classmethod
    def copy(cls, other):
        """The copy constructor."""
        return Point(other.x, other.y)

    def __init__(self, x, y):
        self.x, self.y = x, y # pylint: disable=invalid-name

    def cross(self, other):
        """The cross product of two vectors."""
        return self.x * other.y - self.y * other.x
    def __xor__(self, other):
        return self.cross(other)

    def dot(self, other):
        """The dot product of two vectors."""
        return self.x * other.x + self.y * other.y
    def __mul__(self, other):
        """ When sent a Point, will calculate the dot product, when set a
            escalar, will multiply the point coordinates by that scalar """
        if other.isinstance(Point):
            self.dot(other)
        else:
            Point(self.x * other, self.y * other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other)

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
