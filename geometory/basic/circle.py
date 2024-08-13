import math
from typing import TypeVar

T = TypeVar("T")

from geometory.basic.point import Point


class Circle:
    def __init__(self, center: Point, radius: int):
        self.center = center
        self.r = radius

    def __str__(self):
        return f"<Circle({self.center.x} {self.center.y} {self.r})>"

    def _polar(self, a: T, r: T) -> Point:
        return Point(math.cos(r) * a, math.sin(r) * a)

    def get_diameter(self) -> T:
        return self.r * 2

    def get_area(self) -> T:
        return math.pi * self.r * self.r

    def intersect(self, other: "Circle") -> bool:
        return self.center.dist_euclid(other.center) <= (self.r + other.r)

    def get_cross_point(self, other: "Circle") -> tuple[T, T]:
        if not self.intersect(other):
            return -1
        d = (self.center - other.center).abs()
        a = math.acos((self.r**2 + d**2 - other.r**2) / (2 * self.r * d))
        t = (other.center - self.center).arg()
        p1, p2 = self.center + self._polar(self.r, t + a), self.center + self._polar(
            self.r, t - a
        )
        if p1.x == p2.x and p1.y > p2.y:
            p1, p2 = p2, p1
        elif p1.x > p2.x:
            p1, p2 = p2, p1
        return p1, p2
