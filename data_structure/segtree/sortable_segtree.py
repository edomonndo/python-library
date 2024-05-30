from heapq import *
from typing import TypeVar

T = TypeVar("T")
"""
Global variables
op: Callable[[T,T],T]
e_: T
toggle: Callable[[T],T]
"""


def op(x: T, y: T) -> T:
    pass


e_ = None


def toggle(x: T) -> T:
    pass


def xor64():
    x = 88172645463325252
    while True:
        x = x ^ ((x << 7) & 0xFFFFFFFF)
        x = x ^ (x >> 9)
        yield x & 0xFFFFFFFF


rand = xor64()


class SegNode:
    def __init__(self, key: int, value: T):
        self.key = self.kmin = self.kmax = key
        self.val = self.sum = value
        self.inner_l = self.inner_r = None
        self.outer_l = self.outer_r = None
        self.flip = 0
        self.sz = self.inner_sz = 1
        self.pri = next(rand)

    def __str__(self):
        return f"<SegNode(key={self.key}, val={self.val}, sum={self.sum}, inner=({type(self.inner_l).__name__},{type(self.inner_r).__name__}), outer=({type(self.outer_l).__name__},{type(self.outer_r).__name__}), flip={self.flip})>"

    def toggle(self) -> None:
        self.inner_l, self.inner_r = self.inner_r, self.inner_l
        self.outer_l, self.outer_r = self.outer_r, self.outer_l
        self.sum = toggle(self.sum)
        self.flip ^= 1

    def push_down(self) -> None:
        if not self.flip:
            return
        for SegNode in [self.inner_l, self.inner_r, self.outer_l, self.outer_r]:
            if SegNode:
                SegNode.toggle()
        self.flip = 0

    def update(self) -> None:
        self.sz, self.inner_sz = 0, 1
        self.kmin = self.kmax = self.key
        self.sum = e_
        if self.outer_l:
            self.sum = self.outer_l.sum
            self.sz += self.outer_l.sz
        if self.inner_l:
            self.inner_sz += self.inner_l.inner_sz
            self.sum = op(self.sum, self.inner_l.sum)
            self.kmin = min(self.kmin, self.inner_l.kmin)
            self.kmax = max(self.kmax, self.inner_l.kmax)
        self.sum = op(self.sum, self.val)
        if self.inner_r:
            self.inner_sz += self.inner_r.inner_sz
            self.sum = op(self.sum, self.inner_r.sum)
            self.kmin = min(self.kmin, self.inner_r.kmin)
            self.kmax = max(self.kmax, self.inner_r.kmax)
        if self.outer_r:
            self.sum = op(self.sum, self.outer_r.sum)
            self.sz += self.outer_r.sz
        self.sz += self.inner_sz


class SortableSegtree:
    def __init__(self, V: list[T]):
        self.V = V
        self.root = self._build(0, len(V))

    def _build(self, l: int, r: int) -> SegNode:
        m = (l + r) >> 1
        t = SegNode(self.V[m][0], self.V[m][1])
        t.outer_l = self._build(l, m) if l < m else None
        t.outer_r = self._build(m + 1, r) if m + 1 < r else None
        self._pri_satisfy(t)
        t.update()
        return t

    def _pri_satisfy(self, t: SegNode) -> None:
        if not t.outer_l:
            if not t.outer_r or t.pri > t.outer_r.pri:
                return
            t.pri, t.outer_r.pri = t.outer_r.pri, t.pri
            self._pri_satisfy(t.outer_r)
        elif not t.outer_r:
            if t.pri > t.outer_l.pri:
                return
            t.pri, t.outer_l.pri = t.outer_l.pri, t.pri
            self._pri_satisfy(t.outer_l)
        elif t.outer_l.pri > t.outer_r.pri:
            if t.pri > t.outer_l.pri:
                return
            t.pri, t.outer_l.pri = t.outer_l.pri, t.pri
            self._pri_satisfy(t.outer_l)
        else:
            if t.pri > t.outer_r.pri:
                return
            t.pri, t.outer_r.pri = t.outer_r.pri, t.pri
            self._pri_satisfy(t.outer_r)

    @staticmethod
    def _size(t: SegNode) -> int:
        return t.sz if t else 0

    @classmethod
    def _merge_outer(cls, l: SegNode, r: SegNode) -> SegNode:
        if not l:
            return r
        if not r:
            return l
        l.push_down()
        r.push_down()
        if l.pri > r.pri:
            l.outer_r = cls._merge_outer(l.outer_r, r)
            l.update()
            return l
        else:
            r.outer_l = cls._merge_outer(l, r.outer_l)
            r.update()
            return r

    @classmethod
    def _merge_compress(cls, l: SegNode, r: SegNode) -> SegNode:
        if not l:
            return r
        if not r:
            return l
        l.push_down()
        r.push_down()
        if l.pri < r.pri:
            l, r = r, l
        if l.key < r.kmin:
            l.inner_r = cls._merge_compress(l.inner_r, r)
        elif r.kmax < l.key:
            l.inner_l = cls._merge_compress(l.inner_l, r)
        else:
            rl, rr = cls._split_key(r, l.key)
            l.inner_l = cls._merge_compress(l.inner_l, rl)
            l.inner_r = cls._merge_compress(l.inner_r, rr)
        l.update()
        return l

    @classmethod
    def _split_key(cls, t: SegNode, key: int) -> tuple[SegNode, SegNode]:
        if not t:
            return None, None
        if key < t.kmin:
            return None, t
        if t.kmax <= key:
            return t, None
        t.push_down()
        if key < t.key:
            tl, tr = cls._split_key(t.inner_l, key)
            t.inner_l = tr
            t.update()
            return tl, t
        else:
            tl, tr = cls._split_key(t.inner_r, key)
            t.inner_r = tl
            t.update()
            return t, tr

    @classmethod
    def _split_outer(cls, t: SegNode, i: int) -> tuple[SegNode, SegNode]:
        if not t:
            return None, None
        t.push_down()
        szl = cls._size(t.outer_l)
        szr = szl + t.inner_sz
        if i < szl:
            tl, tr = cls._split_outer(t.outer_l, i)
            t.outer_l = tr
            t.update()
            return tl, t
        elif szr <= i:
            tl, tr = cls._split_outer(t.outer_r, i - szr)
            t.outer_r = tl
            t.update()
            return t, tr
        else:
            tmp_l, tmp_r = t.outer_l, t.outer_r
            t.outer_l = t.outer_r = None
            t1, t2 = cls._split_inner(t, i - szl)
            tl = cls._merge_outer(tmp_l, t1)
            tr = cls._merge_outer(t2, tmp_r)
            return tl, tr

    @classmethod
    def _split_range_outer(
        cls, t: SegNode, l: int, r: int
    ) -> tuple[SegNode, SegNode, SegNode]:
        tl, tr = cls._split_outer(t, l)
        trl, trr = cls._split_outer(tr, r - l)
        return tl, trl, trr

    @classmethod
    def _split_inner(cls, t: SegNode, i: int) -> tuple[SegNode, SegNode]:
        if not t:
            return None, None
        t.push_down()
        szl = cls._size(t.inner_l)
        if i <= szl:
            tl, tr = cls._split_inner(t.inner_l, i)
            t.inner_l = tr
            t.update()
            return tl, t
        else:
            tl, tr = cls._split_inner(t.inner_r, i - szl - 1)
            t.inner_r = tl
            t.update()
            return t, tr

    @classmethod
    def _cut_outer(cls, t: SegNode, i: int) -> tuple[SegNode, SegNode, SegNode]:
        if not t:
            return None, None, None
        t.push_down()
        szl = cls._size(t.outer_l)
        szr = szl + t.inner_sz
        if i < szl:
            tl, tm, tr = cls._cut_outer(t.outer_l, i)
            t.outer_l = tr
            t.update()
            return tl, tm, t
        elif szr <= i:
            tl, tm, tr = cls._cut_outer(t.outer_r, i - szr)
            t.outer_r = tl
            t.update()
            return t, tm, tr
        else:
            tmp_l, tmp_r = t.outer_l, t.outer_r
            t.outer_l = t.outer_r = None
            tl, tm, tr = cls._cut_inner(t, i - szl)
            tl = cls._merge_outer(tmp_l, tl)
            tr = cls._merge_outer(tr, tmp_r)
            return tl, tm, tr

    @classmethod
    def _cut_inner(cls, t: SegNode, i: int) -> tuple[SegNode, SegNode, SegNode]:
        if not t:
            return None, None, None
        t.push_down()
        szl = cls._size(t.inner_l)
        if i < szl:
            tl, tm, tr = cls._cut_inner(t.inner_l, i)
            t.inner_l = tr
            t.update()
            return tl, tm, t
        elif i == szl:
            res = t.inner_l, t, t.inner_r
            t.inner_l = t.inner_r = None
            t.update()
            return res
        else:
            tl, tm, tr = cls._cut_inner(t.inner_r, i - szl - 1)
            t.inner_r = tl
            t.update()
            return t, tm, tr

    @classmethod
    def _query_range_outer(cls, t: SegNode, l: int, r: int) -> T:
        if not t:
            return e_
        if l == 0 and r == t.sz:
            return t.sum
        t.push_down()
        szl = cls._size(t.outer_l)
        szr = szl + t.inner_sz
        left_q = right_q = e_
        if l < szl:
            if r <= szl:
                return cls._query_range_outer(t.outer_l, l, r)
            left_q = cls._query_range_outer(t.outer_l, l, szl)
            l = szl
        if szr < r:
            if szr <= l:
                return cls._query_range_outer(t.outer_r, l - szr, r - szr)
            right_q = cls._query_range_outer(t.outer_r, 0, r - szr)
            r = szr
        res = e_ if l == r else cls._query_range_inner(t, l - szl, r - szl)
        res = op(left_q, res)
        res = op(res, right_q)
        return res

    @classmethod
    def _query_range_inner(cls, t: SegNode, l: int, r: int) -> T:
        if not t:
            return e_
        if l == 0 and r == t.sz:
            return t.sum
        t.push_down()
        szl = cls._size(t.inner_l)
        szr = szl + 1
        left_q = right_q = e_
        if l < szl:
            if r <= szl:
                return cls._query_range_inner(t.inner_l, l, r)
            left_q = cls._query_range_inner(t.inner_l, l, szl)
            l = szl
        if szr < r:
            if szr <= l:
                return cls._query_range_inner(t.inner_r, l - szr, r - szr)
            right_q = cls._query_range_inner(t.inner_r, 0, r - szr)
            r = szr
        res = e_ if l == r else t.val
        res = op(left_q, res)
        res = op(res, right_q)
        return res

    @classmethod
    def _enumerate_outer(cls, t: SegNode, res: list[tuple[int, T]]) -> None:
        if not t:
            return
        t.push_down()
        if t.outer_l:
            cls._enumerate_outer(t.outer_l, res)
        cls.enumerate_inner(t, res)
        if t.outer_r:
            cls._enumerate_outer(t.outer_r, res)

    @classmethod
    def _enumerate_inner(cls, t: SegNode, res: list[tuple[int, T]]) -> None:
        if not t:
            return
        t.push_down()
        if t.inner_l:
            cls._enumerate_inner(t.inner_l, res)
        res.append((t.key, t.val))
        if t.inner_r:
            cls._enumerate_inner(t.inner_r, res)

    @classmethod
    def _sort_inner(cls, t: SegNode) -> SegNode:
        if not t:
            return None
        tl, tr = t.outer_l, t.outer_r
        t.outer_l = t.outer_r = None
        t.push_down()
        if (t.inner_l and t.key < t.inner_l.kmax) or (
            t.inner_r and t.inner_r.kmin < t.key
        ):
            t.toggle()
        res = cls._merge_compress(cls._sort_inner(tl), t)
        res = cls._merge_compress(res, cls._sort_inner(tr))
        return res

    def set(self, i: int, key: int, value: T) -> None:
        tl, tm, tr = self._cut_outer(self.root, i)
        tm.key = key
        tm.val = value
        tm.update()
        self.root = self._merge_outer(tl, self._merge_outer(tm, tr))

    def prod(self, l: int, r: int) -> T:
        if l == r:
            return e_
        return self._query_range_outer(self.root, l, r)

    def prod_all(self) -> T:
        return self.root.sum

    def sort(self, l: int, r: int, descending: bool = False) -> None:
        if l == r:
            return
        tl, tm, tr = self._split_range_outer(self.root, l, r)
        tm = self._sort_inner(tm)
        if descending:
            tm.toggle()
        self.root = self._merge_outer(tl, self._merge_outer(tm, tr))

    def to_list(self):
        res = []
        self._enumerate_outer(self.root, res)
        return res
