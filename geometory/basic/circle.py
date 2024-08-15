import math
from typing import TypeVar, Union

T = TypeVar("T")

from geometory.basic.point import Point


class Circle:
    def __init__(self, center: Point, radius: int):
        self.center = center
        self.r = radius

    @staticmethod
    def from_int(x: T, y: T, radius: int) -> "Circle":
        return Circle(Point(x, y), radius)

    def __str__(self):
        return f"<Circle({self.center.x} {self.center.y} {self.r})>"

    def _polar(self, a: T, r: T) -> Point:
        return Point(math.cos(r) * a, math.sin(r) * a)

    def get_diameter(self) -> T:
        return self.r * 2

    def get_area(self) -> T:
        return math.pi * self.r * self.r

    def is_intersect(self, other: "Circle") -> bool:
        return self.center.dist_euclid(other.center) <= (self.r + other.r)

    def intersect(self, other: "Circle") -> int:
        """返り値は共通接線の数"""
        d2 = (self.center - other.center).norm()
        r2 = (self.r + other.r) ** 2
        if d2 > r2:
            return 4  # 接していない
        if d2 == r2:
            return 3  # 外接
        r2 = (self.r - other.r) ** 2
        if d2 == r2:
            return 1  # 内接
        if d2 < r2:
            return 0  # 内包
        return 2  # 交わる

    def get_cross_point(self, other: "Circle") -> Union[tuple[T, T], int]:
        if not self.is_intersect(other):
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

    @staticmethod
    def from_triangle(x1: T, y1: T, x2: T, y2: T, x3: T, y3: T) -> "Circle":
        a, b, c = Point(x1, y1), Point(x2, y2), Point(x3, y3)
        ab, bc, ca = (a - b).abs(), (b - c).abs(), (c - a).abs()
        center = (a * bc + b * ca + c * ab) / (ab + bc + ca)
        # Line.get_distance_segment_from_point
        vec = b - a
        if vec.dot(center - a) < 0:
            r = (center - a).abs()
        elif vec.dot(b - center) < 0:
            r = (center - b).abs()
        else:
            r = abs(vec.cross(center - a) / vec.abs())
        return Circle(center, r)
