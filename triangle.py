from point import Point


class Triangle:
    """
    Class that represent triangle
    """

    def __init__(self, p1, p2, p3):
        """
        (Triangle, Point, Point, Point) -> NoneType
        Create new point
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_triangle(self):
        """
        (Triangle) -> boolean
        Check if it can be triangle or not
        Return True if it is triangle
        """
        return (self.p3.x - self.p1.x) * (self.p2.y - self.p1.y) != (
                self.p3.y - self.p1.y) * (self.p2.x - self.p1.x)

    def perimeter(self):
        """
        (Triangle) -> float
        Return perimeter of triangle
        """
        return self.p1.distance(self.p2) + self.p2.distance(self.p3) + \
               self.p3.distance(self.p1)

    def area(self):
        """
        (Triangle) -> boolean
        Return area of triangle
        """
        return abs(0.5 * ((self.p1.x - self.p3.x) * (self.p2.y - self.p3.y) - (
                self.p2.x - self.p3.x) * (self.p1.y - self.p3.y)))
