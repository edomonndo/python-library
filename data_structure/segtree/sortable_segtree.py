from heapq import *
from typing import Callable, TypeVar

T = TypeVar("T")
S = TypeVar("S", bound="SegNode")


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


class SortableSegtree:
    def __init__(
        self, op: Callable[[T, T], T], e_: T, toggle: Callable[[T], T], V: list[T]
    ):
        self.op = op
        self.e = e_
        self.toggle = toggle
        self.V = V
        self.root = self._build(0, len(V))

    def _build(self, l: int, r: int) -> S:
        m = (l + r) >> 1
        t = SegNode(self.V[m][0], self.V[m][1])
        t.outer_l = self._build(l, m) if l < m else None
        t.outer_r = self._build(m + 1, r) if m + 1 < r else None
        self._pri_satisfy(t)
        self._update(t)
        return t

    def _pri_satisfy(self, t: S) -> None:
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
    def _size(t: S) -> int:
        return t.sz if t else 0

    def _toggle(self, t: S) -> None:
        t.inner_l, t.inner_r = t.inner_r, t.inner_l
        t.outer_l, t.outer_r = t.outer_r, t.outer_l
        t.sum = self.toggle(t.sum)
        t.flip ^= 1

    def _push_down(self, t: S) -> None:
        if not t.flip:
            return
        for node in [t.inner_l, t.inner_r, t.outer_l, t.outer_r]:
            if node:
                self._toggle(node)
        t.flip = 0

    def _update(self, t: S) -> None:
        t.sz, t.inner_sz = 0, 1
        t.kmin = t.kmax = t.key
        t.sum = self.e
        if t.outer_l:
            t.sum = t.outer_l.sum
            t.sz += t.outer_l.sz
        if t.inner_l:
            t.inner_sz += t.inner_l.inner_sz
            t.sum = self.op(t.sum, t.inner_l.sum)
            t.kmin = min(t.kmin, t.inner_l.kmin)
            t.kmax = max(t.kmax, t.inner_l.kmax)
        t.sum = self.op(t.sum, t.val)
        if t.inner_r:
            t.inner_sz += t.inner_r.inner_sz
            t.sum = self.op(t.sum, t.inner_r.sum)
            t.kmin = min(t.kmin, t.inner_r.kmin)
            t.kmax = max(t.kmax, t.inner_r.kmax)
        if t.outer_r:
            t.sum = self.op(t.sum, t.outer_r.sum)
            t.sz += t.outer_r.sz
        t.sz += t.inner_sz

    def _merge_outer(self, l: S, r: S) -> S:
        if not l:
            return r
        if not r:
            return l
        self._push_down(l)
        self._push_down(r)
        if l.pri > r.pri:
            l.outer_r = self._merge_outer(l.outer_r, r)
            self._update(l)
            return l
        else:
            r.outer_l = self._merge_outer(l, r.outer_l)
            self._update(r)
            return r

    def _merge_compress(self, l: S, r: S) -> S:
        if not l:
            return r
        if not r:
            return l
        self._push_down(l)
        self._push_down(r)
        if l.pri < r.pri:
            l, r = r, l
        if l.key < r.kmin:
            l.inner_r = self._merge_compress(l.inner_r, r)
        elif r.kmax < l.key:
            l.inner_l = self._merge_compress(l.inner_l, r)
        else:
            rl, rr = self._split_key(r, l.key)
            l.inner_l = self._merge_compress(l.inner_l, rl)
            l.inner_r = self._merge_compress(l.inner_r, rr)
        self._update(l)
        return l

    def _split_key(self, t: S, key: int) -> tuple[S, S]:
        if not t:
            return None, None
        if key < t.kmin:
            return None, t
        if t.kmax <= key:
            return t, None
        self._push_down(t)
        if key < t.key:
            tl, tr = self._split_key(t.inner_l, key)
            t.inner_l = tr
            self._update(t)
            return tl, t
        else:
            tl, tr = self._split_key(t.inner_r, key)
            t.inner_r = tl
            self._update(t)
            return t, tr

    def _split_outer(self, t: S, i: int) -> tuple[S, S]:
        if not t:
            return None, None
        self._push_down(t)
        szl = self._size(t.outer_l)
        szr = szl + t.inner_sz
        if i < szl:
            tl, tr = self._split_outer(t.outer_l, i)
            t.outer_l = tr
            self._update(t)
            return tl, t
        elif szr <= i:
            tl, tr = self._split_outer(t.outer_r, i - szr)
            t.outer_r = tl
            self._update(t)
            return t, tr
        else:
            tmp_l, tmp_r = t.outer_l, t.outer_r
            t.outer_l = t.outer_r = None
            t1, t2 = self._split_inner(t, i - szl)
            tl = self._merge_outer(tmp_l, t1)
            tr = self._merge_outer(t2, tmp_r)
            return tl, tr

    def _split_range_outer(self, t: S, l: int, r: int) -> tuple[S, S, S]:
        tl, tr = self._split_outer(t, l)
        trl, trr = self._split_outer(tr, r - l)
        return tl, trl, trr

    def _split_inner(self, t: S, i: int) -> tuple[S, S]:
        if not t:
            return None, None
        self._push_down(t)
        szl = self._size(t.inner_l)
        if i <= szl:
            tl, tr = self._split_inner(t.inner_l, i)
            t.inner_l = tr
            self._update(t)
            return tl, t
        else:
            tl, tr = self._split_inner(t.inner_r, i - szl - 1)
            t.inner_r = tl
            self._update(t)
            return t, tr

    def _cut_outer(self, t: S, i: int) -> tuple[S, S, S]:
        if not t:
            return None, None, None
        self._push_down(t)
        szl = self._size(t.outer_l)
        szr = szl + t.inner_sz
        if i < szl:
            tl, tm, tr = self._cut_outer(t.outer_l, i)
            t.outer_l = tr
            self._update(t)
            return tl, tm, t
        elif szr <= i:
            tl, tm, tr = self._cut_outer(t.outer_r, i - szr)
            t.outer_r = tl
            self._update(t)
            return t, tm, tr
        else:
            tmp_l, tmp_r = t.outer_l, t.outer_r
            t.outer_l = t.outer_r = None
            tl, tm, tr = self._cut_inner(t, i - szl)
            tl = self._merge_outer(tmp_l, tl)
            tr = self._merge_outer(tr, tmp_r)
            return tl, tm, tr

    def _cut_inner(self, t: S, i: int) -> tuple[S, S, S]:
        if not t:
            return None, None, None
        self._push_down(t)
        szl = self._size(t.inner_l)
        if i < szl:
            tl, tm, tr = self._cut_inner(t.inner_l, i)
            t.inner_l = tr
            self._update(t)
            return tl, tm, t
        elif i == szl:
            res = t.inner_l, t, t.inner_r
            t.inner_l = t.inner_r = None
            self._update(t)
            return res
        else:
            tl, tm, tr = self._cut_inner(t.inner_r, i - szl - 1)
            t.inner_r = tl
            self._update(t)
            return t, tm, tr

    def _query_range_outer(self, t: S, l: int, r: int) -> T:
        if not t:
            return self.e
        if l == 0 and r == t.sz:
            return t.sum
        self._push_down(t)
        szl = self._size(t.outer_l)
        szr = szl + t.inner_sz
        left_q = right_q = self.e
        if l < szl:
            if r <= szl:
                return self._query_range_outer(t.outer_l, l, r)
            left_q = self._query_range_outer(t.outer_l, l, szl)
            l = szl
        if szr < r:
            if szr <= l:
                return self._query_range_outer(t.outer_r, l - szr, r - szr)
            right_q = self._query_range_outer(t.outer_r, 0, r - szr)
            r = szr
        res = self.e if l == r else self._query_range_inner(t, l - szl, r - szl)
        res = self.op(left_q, res)
        res = self.op(res, right_q)
        return res

    def _query_range_inner(self, t: S, l: int, r: int) -> T:
        if not t:
            return self.e
        if l == 0 and r == t.sz:
            return t.sum
        self._push_down(t)
        szl = self._size(t.inner_l)
        szr = szl + 1
        left_q = right_q = self.e
        if l < szl:
            if r <= szl:
                return self._query_range_inner(t.inner_l, l, r)
            left_q = self._query_range_inner(t.inner_l, l, szl)
            l = szl
        if szr < r:
            if szr <= l:
                return self._query_range_inner(t.inner_r, l - szr, r - szr)
            right_q = self._query_range_inner(t.inner_r, 0, r - szr)
            r = szr
        res = self.e if l == r else t.val
        res = self.op(left_q, res)
        res = self.op(res, right_q)
        return res

    def _enumerate_outer(self, t: S, res: list[tuple[int, T]]) -> None:
        if not t:
            return
        self._push_down(t)
        if t.outer_l:
            self._enumerate_outer(t.outer_l, res)
        self._enumerate_inner(t, res)
        if t.outer_r:
            self._enumerate_outer(t.outer_r, res)

    def _enumerate_inner(self, t: S, res: list[tuple[int, T]]) -> None:
        if not t:
            return
        self._push_down(t)
        if t.inner_l:
            self._enumerate_inner(t.inner_l, res)
        res.append((t.key, t.val))
        if t.inner_r:
            self._enumerate_inner(t.inner_r, res)

    def _sort_inner(self, t: S) -> S:
        if not t:
            return None
        tl, tr = t.outer_l, t.outer_r
        t.outer_l = t.outer_r = None
        self._push_down(t)
        if (t.inner_l and t.key < t.inner_l.kmax) or (
            t.inner_r and t.inner_r.kmin < t.key
        ):
            self._toggle(t)
        res = self._merge_compress(self._sort_inner(tl), t)
        res = self._merge_compress(res, self._sort_inner(tr))
        return res

    def set(self, i: int, key: int, value: T) -> None:
        tl, tm, tr = self._cut_outer(self.root, i)
        tm.key = key
        tm.val = value
        self._update(tm)
        self.root = self._merge_outer(tl, self._merge_outer(tm, tr))

    def prod(self, l: int, r: int) -> T:
        if l == r:
            return self.e
        return self._query_range_outer(self.root, l, r)

    def prod_all(self) -> T:
        return self.root.sum

    def sort(self, l: int, r: int, descending: bool = False) -> None:
        if l == r:
            return
        tl, tm, tr = self._split_range_outer(self.root, l, r)
        tm = self._sort_inner(tm)
        if descending:
            self._toggle(tm)
        self.root = self._merge_outer(tl, self._merge_outer(tm, tr))

    def to_list(self):
        res = []
        self._enumerate_outer(self.root, res)
        return res
