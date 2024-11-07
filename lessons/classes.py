from math import sqrt


class Coordinate:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_dist(self, other):
        return sqrt(
            ((self.x - other.x) * (self.x - other.x))
            + ((self.y - other.y) * (self.y - other.y))
        )


Coordinate_1: Coordinate = Coordinate(5, 3)
Coordinate_2: Coordinate = Coordinate(1, 2)

Coordinate_1.get_dist(Coordinate_2)
