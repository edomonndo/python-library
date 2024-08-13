import math
from typing import TypeVar

T = TypeVar("T")


class Point:
    EPS = 1e-10

    def __init__(self, x: T, y: T):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter([self.x, self.y])

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k: "Point") -> "Point":
        return Point(self.x * k, self.y * k)

    def __truediv__(self, k: "Point") -> "Point":
        return Point(self.x / k, self.y / k)

    def __floordiv__(self, k: "Point") -> "Point":
        return Point(self.x // k, self.y // k)

    def __eq__(self, other: "Point") -> bool:
        return abs(self.x - other.x) < self.EPS and abs(self.y - other.y) < self.EPS

    def __ne__(self, other: "Point") -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: "Point") -> bool:
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def __gt__(self, other: "Point") -> bool:
        if self.x != other.x:
            return self.x > other.x
        return self.y > other.y

    def __str__(self) -> str:
        return f"<Point({self.x} {self.y})>"

    __repr__ = __str__

    def norm(self) -> T:
        return self.x**2 + self.y**2

    def abs(self) -> float:
        return self.norm() ** 0.5

    def dot(self, other: "Point") -> T:
        """内積"""
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Point") -> T:
        """外積"""
        return self.x * other.y - self.y * other.x

    def dist_euclid(self, other: "Point") -> float:
        """ユークリッド距離"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def dist_manhattan(self, other: "Point") -> T:
        """マンハッタン距離"""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def dist_chebyshev(self, other: "Point") -> T:
        """チェビシェフ距離"""
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def is_orthogonal(self, other: "Point") -> bool:
        """直交判定"""
        return abs(self.dot(other)) < self.EPS

    def is_parallel(self, other: "Point") -> bool:
        """平行判定"""
        return abs(self.cross(other)) < self.EPS

    def ccw(self, other1: "Point", other2: "Point") -> int:
        """自身から点other1に向かうベクトルに対して，点other2の位置を返す.
        COUNTER_CLOCKWISE = 1
        CLOCKWISE = -1
        ONLINE_BACK = 2
        ONLINE_FRONT = -2
        ON_SEGMENT = 0
        """
        a = other1 - self
        b = other2 - self
        if a.cross(b) > self.EPS:
            return 1
        if a.cross(b) < -self.EPS:
            return -1
        if a.dot(b) < -self.EPS:
            return 2
        if a.norm() < b.norm():
            return -2
        return 0

    def arg(self) -> float:
        return math.atan2(self.y, self.x)

    def get(self) -> tuple[T, T]:
        return self.x, self.y

    @classmethod
    def cmp(cls, a: T, b: T, is_float: bool = False) -> int:
        if is_float:
            if a > b + cls.EPS:
                return 1
            if a < b - cls.EPS:
                return -1
            return 0
        else:
            if a > b:
                return 1
            if a < b:
                return -1
            return 0
