from data_structure.fenwick_tree.fenwick_tree import FenwickTree


from collections import deque
from bisect import bisect_left


class StaticRectangleAddPointGet:
    def __init__(self):
        self.rects = []
        self.qs = []

    def add_rect(self, x1: int, y1: int, x2: int, y2: int, w: int) -> None:
        if x1 == x2 or y1 == y2:
            return
        assert x1 <= x2 and y1 <= y2
        self.rects.append((x1, y1, x2, y2, w))

    def add_query(self, x: int, y: int) -> None:
        self.qs.append((x, y))

    def solve(self) -> list[int]:
        n, q = len(self.rects), len(self.qs)
        res = [0] * q
        if n == 0 or q == 0:
            return res

        toY = sorted(set(y for _, y in self.qs))

        event = []
        for x1, y1, x2, y2, w in self.rects:
            y1_ = bisect_left(toY, y1)
            y2_ = bisect_left(toY, y2)
            event += [(x1, y1_, y2_, 0, w), (x2, y1_, y2_, 1, w)]
        event.sort()

        qs = list(range(q))
        qs.sort(key=lambda i: self.qs[i][0])

        j = 0
        bit = FenwickTree(len(toY) + 1)
        for i in qs:
            x, y = self.qs[i]
            while j < n + n and event[j][0] <= x:
                y1, y2, f, w = event[j][1:]
                if f:
                    bit.add(y1, -w)
                    bit.add(y2, w)
                else:
                    bit.add(y1, w)
                    bit.add(y2, -w)
                j += 1
            y = bisect_left(toY, y)
            res[i] = bit._sum(y + 1)

        return res


class OfflineRectangleAddPointGet:
    def __init__(self):
        self.queries = []

    def add_rect(self, x1: int, y1: int, x2: int, y2: int, w: int) -> None:
        if x1 == x2 or y1 == y2:
            return
        assert x1 <= x2 and y1 <= y2
        self.queries.append((x1, y1, x2, y2, w))

    def add_query(self, x: int, y: int) -> None:
        self.queries.append((x, y))

    def solve(self) -> list[int]:
        q = len(self.queries)
        rev = [-1] * q
        sz = 0
        for i in range(q):
            if len(self.queries[i]) == 2:
                rev[i] = sz
                sz += 1

        res = [0] * sz
        st = deque([(0, q)])
        while st:
            l, r = st.popleft()
            m = (l + r) >> 1
            solver = StaticRectangleAddPointGet()
            for k in range(l, m):
                if len(self.queries[k]) > 2:
                    x1, y1, x2, y2, w = self.queries[k]
                    solver.add_rect(x1, y1, x2, y2, w)
            for k in range(m, r):
                if len(self.queries[k]) == 2:
                    x, y = self.queries[k]
                    solver.add_query(x, y)
            sub = solver.solve()
            t = 0
            for k in range(m, r):
                if len(self.queries[k]) == 2:
                    i = rev[k]
                    res[i] += sub[t]
                    t += 1
            if l + 1 < m:
                st.append((l, m))
            if m + 1 < r:
                st.append((m, r))
        return res
