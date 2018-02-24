from point import Point


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_triangle(self):
        return (self.p3.x - self.p1.x) * (self.p2.y - self.p1.y) != (
                self.p3.y - self.p1.y) * (self.p2.x - self.p1.x)

    def perimeter(self):
        return self.p1.distance(self.p2) + self.p2.distance(self.p3) + \
               self.p3.distance(self.p1)

    def area(self):
        return abs(0.5 * ((self.p1.x - self.p3.x) * (self.p2.y - self.p3.y) - (
                self.p2.x - self.p3.x) * (self.p1.y - self.p3.y)))
