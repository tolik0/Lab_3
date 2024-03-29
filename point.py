class Point:
    """
    Class that represent point
    """

    def __init__(self, x=0, y=0):
        """
        (Point, float, float) -> NoneType
        Create new point
        """
        self.x = x
        self.y = y

    def distance(self, p):
        """
        (Point, Point) -> float
        Return distance between two points
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
