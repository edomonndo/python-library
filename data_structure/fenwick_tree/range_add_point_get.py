from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from typing import TypeVar

T = TypeVar("T")


class RangeAddPointGet:
    def __init__(self, n: int, e: T = 0):
        self.n = n
        self.e = e
        self.bit = FenwickTree(n, e)

    def add(self, l: int, r: int, x: T) -> None:
        assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        self.bit.add(l, x)
        if r != self.n:
            self.bit.add(r, -x)

    def get(self, k: int) -> T:
        assert 0 <= k < self.n
        return self.bit.sum0(k + 1)
