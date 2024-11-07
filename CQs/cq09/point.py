from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int):
        new_point: Point = Point(self.x, self.y)
        self.x = self.x * factor
        self.y = self.y * factor
        return new_point
