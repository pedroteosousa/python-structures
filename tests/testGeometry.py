# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-many-public-methods

import unittest
from math import trunc, atan2
from structures.Geometry import Point, Segment

class testPoint(unittest.TestCase):
    def setUp(self):
        self.p, self.g = Point(4, -2 ** 0.5), Point(1/3, -7)

    def test_constructors(self):
        # number constructor
        self.assertEqual(Point(), (0, 0))
        self.assertEqual(Point(3.9, -7), (3.9, -7))
        # copy constructor
        p = Point(-5, 9)
        self.assertEqual(Point(p), p)
        # from list
        l = [5.2, 6]
        self.assertEqual(Point(l), l)
        # from tuple
        l = (1 / 3, 99.5)
        self.assertEqual(Point(l), l)
        # from complex
        l = complex(5, -7.5)
        self.assertEqual(Point(l), l)

    def test_equal(self):
        p = Point(10, -0.3)
        # two points
        self.assertTrue(p == Point(10, -0.3))
        # point and tuple
        self.assertTrue(p == (p.x, p.y))
        # point and array
        self.assertTrue(p == [p.x, p.y])
        # point and complex
        self.assertTrue(p == complex(p.x, p.y))

    def test_not_equal(self):
        self.assertNotEqual(Point(), Point(0, 0.0000005))

    def test_less(self):
        self.assertLess(Point(), Point(0, 1))
        self.assertLess(Point(), Point(1, 0))

    def test_less_or_equal(self):
        self.assertLessEqual(Point(0, 0), Point(0, 1))
        self.assertLessEqual(Point(0, 0), Point(1, 0))
        self.assertLessEqual(Point(1, 1), Point(1, 1))

    def test_greater(self):
        self.assertGreater(Point(0, 0), Point(0, -1))
        self.assertGreater(Point(0, 0), Point(-1, 0))

    def test_greater_or_equal(self):
        self.assertGreaterEqual(Point(0, 0), Point(0, -1))
        self.assertGreaterEqual(Point(0, 0), Point(-1, 0))
        self.assertGreaterEqual(Point(1, 1), Point(1, 1))

    def test_add(self):
        p, g = self.p, self.g
        self.assertEqual(p + g, (p.x + g.x, p.y + g.y))
        # commutative
        self.assertEqual(g + p, p + g)
        # with tuple
        self.assertEqual(p + g, p + tuple(g))
        self.assertEqual(p + g, tuple(g) + p)
        # iadd
        f = p + g
        p += g
        self.assertEqual(p, f)

    def test_sub(self):
        p, g = self.p, self.g
        self.assertEqual(p - g, (p.x - g.x, p.y - g.y))
        # with tuple
        self.assertEqual(p - g, p - tuple(g))
        self.assertEqual(g - p, tuple(g) - p)
        # isub
        f = p - g
        p -= g
        self.assertEqual(p, f)

    def test_div(self):
        p = self.p
        self.assertEqual(p / 2, (p.x / 2, p.y / 2))
        # floor div
        self.assertEqual(p // 2, (p.x // 2, p.y // 2))
        # idiv
        g = Point(p)
        g /= 2
        self.assertEqual(g, p / 2)
        # ifloordiv
        g = Point(p)
        g //= 2
        self.assertEqual(g, p // 2)

    def test_mul(self):
        p = self.p
        self.assertEqual(p * 2, (p.x * 2, p.y * 2))
        # rmul
        self.assertEqual(2 * p, p * 2)
        # imul
        g = Point(p)
        g *= 2
        self.assertEqual(g, p * 2)

    def test_mod(self):
        p = self.p
        self.assertEqual(p % 2, (p.x % 2, p.y % 2))
        # imod
        g = Point(p)
        g %= 2
        self.assertEqual(g, p % 2)

    def test_unary(self):
        # pylint: disable=invalid-unary-operand-type
        p = self.p
        self.assertEqual(+p, p)
        self.assertEqual(-p, (-p.x, -p.y))
        self.assertEqual(-(-p), p) # pylint: disable=nonexistent-operator

    def test_normalize(self):
        p = Point(1/3, 2 ** 0.5)
        # check if colinear and length 1
        self.assertEqual(p ** p.normalized(), 0)
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
        self.assertEqual(p.cross(g), p ** g)

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

class testSegment(unittest.TestCase):
    def test_constructors(self):
        p, q = Point(2, 1 / 3), Point(-3, 1.5)
        s = Segment(p, q)
        self.assertEqual((q, p), (s.a, s.b))

    def test_len(self):
        p, q = Point(2, 1), Point(0, 3)
        s = Segment(p, q)
        self.assertEqual(abs(s), 8 ** 0.5)
        # len
        self.assertEqual(abs(s), s.len())

    def test_contains(self):
        p, q = Point(2, 2), Point(-3, 1)
        s = Segment(p, q)
        # middle
        self.assertTrue(Point(-0.5, 1.5) in s)
        # borders
        self.assertTrue(p in s)
        self.assertTrue(q in s)
        # outside
        self.assertFalse(Point(0, 0) in s)
        self.assertFalse(Point(2.0000001, 2.0000001) in s)

    def test_intersection(self):
        p, q = Point(2, 2), Point(-3, 1)
        m = (p + q) / 2
        s = Segment(p, q)
        # point
        self.assertEqual(s.intersection(m), m)
        self.assertEqual(s.intersection(Point()), None)
        # segment
        t = Segment(m, Point(-8, 0))
        self.assertEqual(s.intersection(t), Segment(m, q))
        self.assertEqual(s.intersection(Segment(Point(), p)), p)
        self.assertEqual(s.intersection(Segment(Point(-0.5, 0), Point(-0.5, 2))), m)
        self.assertEqual(s.intersection(Segment(Point(), Point(1, 1))), None)

    def test_pin(self):
        p, q = Point(2 ** 0.5, -1), Point(-7, 3.5)
        self.assertEqual(p - q, Segment(p, q).pin())

if __name__ == '__main__':
    unittest.main()
