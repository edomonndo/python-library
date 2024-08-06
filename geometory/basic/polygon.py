from geometory.basic.point import Point
from geometory.basic.line import Line

from typing import TypeVar

T = TypeVar("T")


class Polygon:
    def __init__(self, arr: list[Point]):
        """
        配列arrは，多角形の隣り合った点を反時計回りに訪問する順番であること．
        """
        self.arr = arr
        self.n = len(arr)

    def __len__(self) -> int:
        return self.n

    def __getitem__(self, idx: int) -> Point:
        return self.arr[idx]

    def contains(self, p: Point) -> int:
        """
        点pが多角形に内包されているか判定
        IN 2
        ON 1
        OUT 0
        """
        x = 0
        for i in range(self.n):
            a = self.arr[i] - p
            b = self.arr[(i + 1) % self.n] - p
            if abs(a.cross(b)) < p.EPS and a.dot(b) < p.EPS:
                return 1
            if a.y > b.y:
                a, b = b, a
            if a.y < p.EPS and p.EPS < b.y and a.cross(b) > p.EPS:
                x ^= 1
        return 2 if x else 0

    def is_convex(self) -> bool:
        for i in range(self.n):
            pre = (i - 1) % self.n
            nex = (i + 1) % self.n
            if self.arr[pre].ccw(self.arr[i], self.arr[nex]) == -1:
                return False
        return True

    def area(self) -> T:
        res = self.arr[-1].cross(self.arr[0])
        for i in range(self.n - 1):
            res += self.arr[i].cross(self.arr[i + 1])
        return abs(res) / 2

    def divide_by_segment(self, seg: Line) -> int:
        lines = [Line(self.arr[i], self.arr[(i + 1) % self.n]) for i in range(self.n)]
        cnt = sum(1 for line in lines if line.intersect(seg))
        return (cnt >> 1) + 1

    def convex_hull(ps: list[Point]) -> list[Point]:

        ps = list(set(ps))
        if len(ps) <= 2:
            return ps

        ps.sort()
        res = []

        def cross3(a: Point, b: Point, c: Point) -> int:
            return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

        for p in ps:
            while len(res) > 1 and cross3(res[-1], res[-2], p) >= 0:
                res.pop()
            res.append(p)

        sz = len(res)
        for p in ps[::-1][1:]:
            while len(res) > sz and cross3(res[-1], res[-2], p) >= 0:
                res.pop()
            res.append(p)
        res.pop()
        return res
