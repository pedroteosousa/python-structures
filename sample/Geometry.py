# pylint: disable=invalid-name

""" Implementations of various geometry data structures. """

from math import sqrt

class Point(object):
    """ Point in 2D space. """

    def __init__(self, x=0, y=0):
        """ Class constructor. """
        if isinstance(x, Point):
            self.x, self.y = x.x, x.y
        elif isinstance(x, (type([]), type(()))): # check if x is a list or a tuple
            self.x, self.y = x
        else:
            self.x, self.y = x, y

    def __iter__(self):
        return iter((self.x, self.y))
    def __getitem__(self, idx):
        return tuple(self)[idx]

    def __eq__(self, other):
        return tuple(self) == tuple(other)
    def __ne__(self, other):
        return tuple(self) != tuple(other)
    def __lt__(self, other):
        return tuple(self) < tuple(other)
    def __gt__(self, other):
        return tuple(self) > tuple(other)
    def __le__(self, other):
        return tuple(self) <= tuple(other)
    def __ge__(self, other):
        return tuple(self) >= tuple(other)

    def cross(self, other):
        """ The cross product of two Points. """
        return self.x * other.y - self.y * other.x
    def __xor__(self, other):
        """ Another way to use cross. """
        return self.cross(other)

    def dot(self, other):
        """ The dot product of two Points. """
        return self.x * other.x + self.y * other.y
    def __mul__(self, other):
        """ When sent a Point, will calculate the dot product, when sent a
            escalar, will multiply the point coordinates by that scalar """
        if isinstance(other, Point):
            return self.dot(other)
        return Point(self.x * other, self.y * other)

    def __add__(self, other):
        """ Adds two Points. """
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        """ Subtracts two Points. """
        return Point(self.x - other.x, self.y - other)

    def __abs__(self):
        """ Distance to (0, 0). """
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        """ String representation of a Point. """
        return str(tuple(self))
