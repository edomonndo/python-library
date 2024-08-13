from typing import TypeVar, Callable

from data_structure.segtree.segment_tree import Segtree
from data_structure.basic.wordsize_tree_set import WordsizeTreeSet

T = TypeVar("T")


class RangeSetRangeComposite:
    def __init__(
        self,
        op: Callable[[T, T], T],
        e: T,
        pow_: Callable[[T, int], T],
        id_: T,
        A: list[T],
    ):
        self.op = op
        self.e = e
        self.pow = pow_
        self.id = id_
        self.seg = Segtree(A + [e], op, e)
        self.n = len(A) + 1
        self.idx = WordsizeTreeSet(self.n + 1, range(self.n + 1))
        self.val = A + [e]
        self.beki = [1] * self.n

    def prod(self, l: int, r: int) -> T:
        assert 0 <= l < r <= self.n
        idx, beki, op = self.idx, self.beki, self.op
        pow, val, seg = self.pow, self.val, self.seg
        l1 = idx.ge(l)
        r1 = idx.le(r)
        res = self.e
        if l1 != l:
            l0 = idx.le(l)
            beki = beki[l0] - (l - l0) if l0 + beki[l0] <= r else r - l
            res = pow(val[l0], beki)
        if l1 < r1:
            res = op(res, seg.prod(l1, r1))
        if r1 != r and l <= r1:
            res = op(res, pow(val[r1], r - r1))
        return res

    def apply(self, l: int, r: int, f: T) -> None:
        idx, val, beki, seg, pow = self.idx, self.val, self.beki, self.seg, self.pow

        l0, r0 = idx.le(l), idx.le(r)
        if l != l0:
            seg.set(l0, pow(val[l0], l - l0))
        if r != r0:
            beki[r] = beki[r0] - (r - r0)
            idx.add(r)
            val[r] = val[r0]
            seg.set(r, pow(val[r], beki[r]))
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
        seg.set(l, pow(f, beki[l]))
