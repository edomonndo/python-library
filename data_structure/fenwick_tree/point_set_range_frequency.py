from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from bisect import bisect_left


class PointSetRangeFrequency:

    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.dat = arr
        self.qs = qs = []
        for i, a in enumerate(arr):
            qs.append((0, 1, a * self.n + i))

    def add_set_query(self, p: int, x: int):
        assert 0 <= p < self.n
        self.qs.append((0, -1, self.dat[p] * self.n + p))
        self.dat[p] = x
        self.qs.append((0, 1, x * self.n + p))

    def add_freq_query(self, l: int, r: int, x: int):
        assert 0 <= l <= r <= self.n
        self.qs.append((1, x * self.n + l, x * self.n + r))

    def solve(self) -> list[int]:
        qs = self.qs
        vs = sorted(set([b for t, _, b in qs if t == 0]))
        bit = FenwickTree(len(vs) + 1)
        res = []
        for t, a, b in qs:
            if t == 0:
                z = bisect_left(vs, b)
                bit.add(z, a)
            else:
                l = bisect_left(vs, a)
                r = bisect_left(vs, b)
                res.append(bit.sum(l, r))
        return res
