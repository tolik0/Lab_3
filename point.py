class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5