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

    def __set(self, other):
        """ Update self instance with another value. """
        self.__dict__.update(other.__dict__)
        return self

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

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        """ Adds two Points. """
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        """ Subtracts two Points. """
        return Point(self.x - other.x, self.y - other.y)
    def __truediv__(self, other):
        """ Divides a point by a scalar. """
        return Point(self.x / other, self.y / other)
    def __floordiv__(self, other):
        """ Integer division. """
        return Point(self.x // other, self.y // other)
    def __mod__(self, other):
        """ Takes mod. """
        return Point(self.x % other, self.y % other)

    def __iadd__(self, other):
        return self.__set(self + other)
    def __isub__(self, other):
        return self.__set(self - other)
    def __itruediv__(self, other):
        return self.__set(self / other)
    def __ifloordiv__(self, other):
        return self.__set(self // other)
    def __imod__(self, other):
        return self.__set(self % other)
    def __imul__(self, other):
        return self.__set(self * other)

    def __abs__(self):
        """ Distance to (0, 0). """
        return sqrt(self.x ** 2 + self.y ** 2)
    def len(self):
        """ Distance to (0, 0). """
        return abs(self)

    def __int__(self):
        """ Truncate to int. """
        return Point(int(self.x), int(self.y))
    def __long__(self):
        """ Truncate to long. """
        return Point(long(self.x), long(self.y))
    def __complex__(self):
        """ Convert to complex. """
        return complex(self.x, self.y)
    def __trunc__(self):
        return long(self)

    def normalized(self):
        """ Normalized vector from origin to this Point. """
        length = abs(self)
        return Point() if length == 0 else self / abs(self)
    def normalize(self):
        """ Normalizes this Point. """
        return self.__set(self.normalized())

    def __str__(self):
        """ String representation of a Point. """
        return str(tuple(self))
