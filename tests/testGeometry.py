# pylint: disable=invalid-name
# pylint: disable=missing-docstring

import unittest
from math import trunc, atan2
from structures.Geometry import Point

class testPoint(unittest.TestCase):
    def compare_point(self, p, l):
        self.assertEqual((p.x, p.y), l)

    def test_constructors(self):
        # default constructor
        self.compare_point(Point(), (0, 0))
        # one number constructor
        self.compare_point(Point(10), (10, 0))
        # two numbers constructor
        self.compare_point(Point(3.9, -7), (3.9, -7))
        # copy constructor
        p = Point(-5, 9)
        self.compare_point(Point(p), (p.x, p.y))
        # from list
        l = [5.2, 6]
        self.compare_point(Point(l), tuple(l))
        # from tuple
        l = (1 / 3, 99.5)
        self.compare_point(Point(l), l)
        # from complex
        l = complex(5, -7.5)
        self.compare_point(Point(l), (l.real, l.imag))

    def test_cmp(self):
        # equal
        self.assertEqual(Point(1 / 3, -1), Point(1 / 3, -1))
        # not equal
        self.assertNotEqual(Point(), Point(0, 0.0000005))
        # less and less or equal
        self.assertLess(Point(0, 0), Point(0, 1))
        self.assertLess(Point(0, 0), Point(1, 0))
        self.assertLessEqual(Point(0, 0), Point(0, 1))
        self.assertLessEqual(Point(0, 0), Point(1, 0))
        self.assertLessEqual(Point(1, 1), Point(1, 1))
        # greater than
        self.assertGreater(Point(0, 0), Point(0, -1))
        self.assertGreater(Point(0, 0), Point(-1, 0))
        self.assertGreaterEqual(Point(0, 0), Point(0, -1))
        self.assertGreaterEqual(Point(0, 0), Point(-1, 0))
        self.assertGreaterEqual(Point(1, 1), Point(1, 1))

    def test_arithmetic(self):
        p, g = Point(4, -2 ** 0.5), Point(1/3, -7)
        # add
        self.assertEqual(p + g, Point(p.x + g.x, p.y + g.y))
        self.assertEqual(g + p, p + g)
        f = Point(p)
        f += g
        self.assertEqual(p + g, f)
        # sub
        self.assertEqual(p - g, Point(p.x - g.x, p.y - g.y))
        f = Point(p)
        f -= g
        self.assertEqual(p - g, f)
        # div
        self.assertEqual(p / 2, Point(p.x / 2, p.y / 2))
        f = Point(p)
        f /= 2
        self.assertEqual(p / 2, f)
        # floor div
        self.assertEqual(p // 2, Point(p.x // 2, p.y // 2))
        f = Point(p)
        f //= 2
        self.assertEqual(p // 2, f)
        # mul
        self.assertEqual(p * 2, Point(p.x * 2, p.y * 2))
        f = Point(p)
        f *= 2
        self.assertEqual(p * 2, f)
        # reflected mul
        self.assertEqual(p * 2, 2 * p)
        # mod
        self.assertEqual(p % 2, Point(p.x % 2, p.y % 2))
        f = Point(p)
        f %= 2
        self.assertEqual(p % 2, f)

    def test_normalize(self):
        p = Point(1/3, 2 ** 0.5)
        # check if colinear and length 1
        self.assertEqual(p ^ p.normalized(), 0)
        self.assertAlmostEqual(abs(p.normalized()), 1)
        # normalize
        g = Point(p)
        f = g.normalize()
        self.assertNotEqual(g, p)
        self.assertEqual(g, f)
        self.assertEqual(g, p.normalized())
        # zero vector
        self.assertEqual(Point(), Point().normalized())

    def test_ang(self):
        p = Point(3, -5)
        self.assertEqual(p.ang(), atan2(p.x, p.y))

    def test_cross(self):
        # left side
        self.assertGreater(Point(1, 1).cross(Point(-1, 5)), 0)
        # right side
        self.assertLess(Point(-3, -8).cross(Point(-3, -3)), 0)
        # colinear
        self.assertEqual(Point(2, 3).cross(Point(-1, -1.5)), 0)
        # using xor
        p, g = Point(2, 40), Point(5, -1 / 3)
        self.assertEqual(p.cross(g), p ^ g)

    def test_dot(self):
        self.assertEqual(Point(1, 1).dot(Point(0, 1)), 1)
        # colinear
        self.assertEqual(Point(1, 1).dot(Point(2, 2)), 4)
        # perpendicular
        self.assertEqual(Point(1, 1).dot(Point(1, -1)), 0)
        # using mul
        p, g = Point(2, 40), Point(5, -1 / 3)
        self.assertEqual(p.dot(g), p * g)

    def test_conversion(self):
        p = Point(-7, 4 / 3)
        # complex
        self.assertEqual(complex(p), complex(p.x, p.y))
        # trunc
        self.assertEqual(trunc(p), Point(-7, 1))

    def test_abs(self):
        # origin
        self.assertEqual(abs(Point(0, 0)), 0)
        # 3 4 5
        self.assertEqual(abs(Point(3, 4)), 5)
        # sqrt 2
        self.assertEqual(abs(Point(-1, 1)), 2 ** 0.5)
        # len
        p = Point(5, 7)
        self.assertEqual(p.len(), abs(p))

    def test_iter(self):
        t = (3, -9)
        p = Point(t)
        for idx, val in enumerate(p):
            self.assertEqual(val, t[idx])
            self.assertEqual(p[idx], t[idx])

    def test_str(self):
        t = (1 / 3, 2 ** 64)
        self.assertEqual(str(Point(t)), str(t))

if __name__ == '__main__':
    unittest.main()
