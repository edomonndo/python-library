from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from data_structure.fenwick_tree.cumulative_sum import CumulativeSum
from typing import TypeVar

T = TypeVar("T")


class RangeAddRangeSum:
    def __init__(self, arr: list[int], e: T = 0):
        self.n = n = len(arr)
        self.e = e
        self.bit1 = FenwickTree(n, e)
        self.bit2 = FenwickTree(n, e)
        self.cs = CumulativeSum(arr)

    def add(self, l: int, r: int, x: T) -> None:
        assert 0 <= l <= r <= self.n
        self.bit1.add(l, x)
        self.bit2.add(l, -x * self.cs.prod(0, l))
        if r != self.n:
            self.bit1.add(r, -x)
            self.bit2.add(r, x * self.cs.prod(0, r))

    def _prod(self, k: int) -> T:
        return self.bit1.sum0(k) * self.cs.prod(0, k) + self.bit2.sum0(k)

    def sum(self, l: int, r: int) -> T:
        assert 0 <= l <= r <= self.n
        return self._prod(r) - self._prod(l)

    def set(self, k: int, x: T) -> None:
        self.add(k, k + 1, x - self.sum(k, k + 1))
