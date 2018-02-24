import unittest
from triangle import Triangle, Point


class triangle_test(unittest.TestCase):

    def test_is_triangle(self):
        p1 = Point(0, 0)
        p2 = Point(1, 1)
        p3 = Point(2, 2)
        t = Triangle(p1, p2, p3)
        self.assertEqual(t.is_triangle(), False)

    def test_perimeter(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        p3 = Point(3, 0)
        t = Triangle(p1, p2, p3)
        self.assertEqual(t.perimeter(), 12)

    def test_area(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        p3 = Point(3, 0)
        t = Triangle(p1, p2, p3)
        self.assertEqual(t.area(), 6)


if __name__ == '__main__':
    unittest.main()
