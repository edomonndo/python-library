from typing import Union, TypeVar

T = TypeVar("T")

from geometory.basic.point import Point
from geometory.basic.circle import Circle


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.EPS = 1e-10
        self.s = p1
        self.t = p2
        self.vector = p2 - p1

    def __str__(self):
        return f"<Line({self.s.x} {self.s.y} {self.t.x} {self.t.y})>"

    @classmethod
    def from_int(cls, x1: T, y1: T, x2: T, y2: T) -> "Line":
        return Line(Point(x1, y1), Point(x2, y2))

    def is_orthogonal(self, other: "Line") -> bool:
        return abs(self.vector.dot(other.vector)) < self.EPS

    def is_parallel(self, other: "Line") -> bool:
        return abs(self.vector.cross(other.vector)) < self.EPS

    def project_from_point(self, point: Point) -> Point:
        """直線に点pointから垂線を引いたときの交点"""
        r = self.vector.dot(point - self.s) / self.vector.norm()
        return self.s + self.vector * r

    def project(self, x: T, y: T) -> Point:
        return self.project_from_point(Point(x, y))

    def refrection_from_point(self, point: Point) -> Point:
        """直線を対称軸として，点pointと線対称な点の座標"""
        return point + (self.project(point) - point) * 2

    def refrection(self, x: T, y: T) -> Point:
        return self.project_from_point(Point(x, y))

    def get_distance_from_point(self, point: Point) -> T:
        """直線と点のユークリッド距離"""
        return abs(self.vector.cross(point - self.s) / self.vector.abs())

    def get_distance(self, x: T, y: T) -> T:
        return self.get_distance_from_point(Point(x, y))

    def get_distance_segment_from_point(self, point: Point) -> T:
        """線分と点のユークリッド距離"""
        if self.vector.dot(point - self.s) < 0:
            p = point - self.s
            return p.abs()
        if self.vector.dot(self.t - point) < 0:
            p = point - self.t
            return p.abs()
        return self.get_distance_from_point(point)

    def get_distance_segment(self, x: T, y: T) -> T:
        return self.get_distance_segment_from_point(Point(x, y))

    def get_distance_seg_to_seg(self, other: "Line") -> int:
        """線分と線分のユークリッド距離"""
        if self.intersect(other):
            return 0
        return min(
            self.get_distance_segment_from_point(other.s),
            self.get_distance_segment_from_point(other.t),
            other.get_distance_segment_from_point(self.s),
            other.get_distance_segment_from_point(self.t),
        )

    def intersect(self, other: Union["Line", Circle]) -> bool:
        if isinstance(other, Line):
            return (
                self.s.ccw(self.t, other.s) * self.s.ccw(self.t, other.t) <= 0
                and other.s.ccw(other.t, self.s) * other.s.ccw(other.t, self.t) <= 0
            )
        if isinstance(other, Circle):
            return self.get_distance_from_point(other.center) <= other.r
        raise TypeError

    def get_cross_point(self, other: Union["Line", Circle]) -> Union[Point, int]:
        if isinstance(other, Line):
            if not self.intersect(other):
                return -1
            d1 = abs(other.vector.cross(self.s - other.t))
            d2 = abs(other.vector.cross(self.t - other.t))
            t = d1 / (d1 + d2)
            return self.s + (self.vector) * t
        if isinstance(other, Circle):
            if not self.intersect(other):
                return -1
            pr = self.project(other.center)
            e = self.vector / self.vector.abs()
            base = (other.r**2 - (pr - other.center).norm()) ** 0.5
            p1, p2 = pr + e * base, pr - e * base
            if p1.x == p2.x:
                return (p1, p2) if p1.y < p2.y else (p2, p1)
            if p1.x < p2.x:
                return (p1, p2)
            return (p2, p1)
        raise TypeError
