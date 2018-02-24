import unittest
from point import Point


class point_test(unittest.TestCase):

    def test_distance(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertEqual(p1.distance(p2), 5.0)


if __name__ == '__main__':
    unittest.main()
