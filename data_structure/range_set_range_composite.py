from typing import Callable
from atcoder.segtree import SegTree
from data_structure.basic.SortedMultiset import SortedMultiset


class RangeSetRangeComposite:
    def __init__(
        self,
        op: Callable[[int, int], int],
        e: int,
        pow_: Callable[[int, int], int],
        id_: int,
        A: list[int],
    ):
        self.op = op
        self.e = e
        self.pow = pow_
        self.id = id_
        self.seg = SegTree(op, e, A + [e])
        self.n = len(A) + 1
        self.idx = SortedMultiset(range(self.n + 1))
        self.val = A + [e]
        self.beki = [1] * self.n

    def prod(self, l: int, r: int) -> int:
        assert 0 <= l < r <= self.n
        l1 = self.idx.ge(l)
        r1 = self.idx.le(r)
        res = self.e
        if l1 != l:
            l0 = self.idx.le(l)
            beki = self.beki[l0] - (l - l0) if l0 + self.beki[l0] <= r else r - l
            res = self.pow(self.val[l0], beki)
        if l1 < r1:
            res = self.op(res, self.seg.prod(l1, r1))
        if r1 != r and l <= r1:
            res = self.op(res, self.pow(self.val[r1], r - r1))
        return res

    def apply(self, l: int, r: int, f: int) -> None:
        idx, val, beki, seg = self.idx, self.val, self.beki, self.seg

        l0, r0 = idx.le(l), idx.le(r)
        if l != l0:
            seg.set(l0, self.pow(val[l0], l - l0))
        if r != r0:
            beki[r] = beki[r0] - (r - r0)
            idx.add(r)
            val[r] = val[r0]
            seg.set(r, self.pow(val[r], beki[r]))
        if l != l0:
            beki[l0] = l - l0

        i = idx.gt(l)
        while i < r:
            seg.set(i, self.e)
            idx.discard(i)
            i = idx.gt(i)
        val[l] = f
        idx.add(l)
        beki[l] = r - l
        seg.set(l, self.pow(f, beki[l]))
