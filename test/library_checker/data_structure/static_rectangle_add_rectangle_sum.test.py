# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
from collections import deque
import typing


class FenwickTree:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


MOD = 998244353


class StaticRectangleAddRectangleSum:
    def __init__(self, n: int, q: int):
        self.X = [0] * (n << 1)
        self.rects = [0] * n
        self.qs = [0] * q
        self.pid = 0
        self.qid = 0

    def add_rect(self, x1: int, y1: int, x2: int, y2: int, w: int) -> None:
        i = self.pid
        self.X[i << 1 | 0] = x1
        self.X[i << 1 | 1] = x2
        self.rects[i] = (x1, y1, x2, y2, w)
        self.pid += 1

    def add_query(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.qs[self.qid] = (x1, y1, x2, y2)
        self.qid += 1

    def solve(self) -> list[int]:
        dX = {x: i for i, x in enumerate(sorted(set(self.X)))}

        # イベントソート
        event = [0] * (self.pid << 1)
        for i, (x1, y1, x2, y2, w) in enumerate(self.rects):
            l, r = dX[x1], dX[x2]
            event[i << 1 | 0] = (y1, l, r, w)
            event[i << 1 | 1] = (y2, l, r, -w)
        event.sort(key=lambda e: e[0])
        event = deque(event)

        bit = [[0, 0] for _ in range(self.pid << 1)]
        pq = [0] * (self.qid << 1)
        for i, (x1, y1, x2, y2) in enumerate(self.qs):
            pq[i << 1 | 0] = (y1, i, 0)
            pq[i << 1 | 1] = (y2, i, 1)
        pq.sort(key=lambda q: q[0])

        res = [0] * self.qid
        for qy, qi, t in pq:
            while event:
                py, pl, pr, w = event.popleft()
                if py < qy:
                    event.appendleft((py, pl, pr, w))
                    break
                wy = w * py % MOD
