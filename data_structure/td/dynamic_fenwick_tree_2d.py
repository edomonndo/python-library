from collections import defaultdict
from typing import TypeVar

T = TypeVar("T")


class DynamicFenwickTree2d:
    def __init__(self, h: int, w: int, e: T):
        self.h = h
        self.w = w
        self.dat = defaultdict(lambda: defaultdict(lambda: e))
        self.e = e

    def add_point(self, x: int, y: int, w: T) -> T:
        dat = self.dat
        x += 1
        y += 1
        while x <= self.h:
            node = dat[x]
            y1 = y
            while y1 <= self.w:
                node[y1] += w
                y1 += y1 & -y1
            x += x & -x

    def add_rect(self, x1: int, y1: int, x2: int, y2: int, w: T) -> None:
        self.add_point(x1, y1, w)
        self.add_point(x1, y2 + 1, -w)
        self.add_point(x2 + 1, y1, -w)
        self.add_point(x2 + 1, y2 + 1, w)

    def sum0(self, x: int, y: int) -> T:
        dat = self.dat
        x = min(x + 1, self.h)
        y = min(y + 1, self.w)
        res = self.e
        while x > 0:
            if x in dat:
                node = dat[x]
                y1 = y
                while y1 > 0:
                    if y1 in node:
                        res += node[y1]
                    y1 -= y1 & -y1
            x -= x & -x
        return res

    def sum(self, x1: int, y1: int, x2: int, y2: int) -> T:
        sum0 = self.sum0
        return sum0(x2, y2) - sum0(x1 - 1, y2) - sum0(x2, y1 - 1) + sum0(x1 - 1, y1 - 1)
