from atcoder.segtree import SegTree
from typing import TypeVar, Callable

T = TypeVar("T")


class CompressedSegtree:
    def __init__(self, op: Callable[[int, int], T], e: T, V: dict[int, T]):
        self.V = V
        self.toIdx = {v: i for i, v in enumerate(sorted(set(V.keys())))}
        toV = list(self.toIdx.keys())
        self.n = len(self.toIdx)
        self.seg = SegTree(op, e, [V[toV[i]] for i in range(self.n)])

    def set(self, p: int, x: T) -> None:
        p = self.toIdx[p]
        self.seg.set(p, x)

    __setitem__ = set

    def get(self, p: int) -> T:
        p = self.toIdx[p]
        return self.seg.get(p)

    __getitem__ = get

    def prod(self, l: int, r: int) -> None:
        l, r = self.toIdx[l], self.toIdx[r]
        return self.seg(l, r)

    def all_prod(self):
        return self.seg.all_prod()
