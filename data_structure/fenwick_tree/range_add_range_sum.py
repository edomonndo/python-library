from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from typing import TypeVar

T = TypeVar("T")


class RangeAddRangeSum:
    def __init__(self, arr: list[int], e: T = 0):
        self.n = n = len(arr)
        self.e = e
        self.bit1 = FenwickTree(n, e)
        self.bit2 = FenwickTree(n, e)

    def add(self, l: int, r: int, x: T) -> None:
        assert 0 <= l <= r <= self.n
        self.bit1.add(l, -x * l)
        self.bit2.add(l, x)
        if r != self.n:
            self.bit1.add(r, x * r)
            self.bit2.add(r, -x)

    def sum(self, l: int, r: int) -> T:
        assert 0 <= l <= r <= self.n
        rsum = self.bit2.sum0(r) * r + self.bit1.sum0(r)
        lsum = self.bit2.sum0(l) * l + self.bit1.sum0(l)
        return rsum - lsum
