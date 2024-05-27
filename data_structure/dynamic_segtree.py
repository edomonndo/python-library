import sys

sys.setrecursionlimit(10**6)

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")

from typing import TypeVar, Callable

T = TypeVar("T")


class SegtreeNode:
    def __init__(self, i: int, value: T):
        self.idx = i
        self.value = value
        self.product = value
        self.l = None
        self.r = None


class DynamicSegtree:
    def __init__(self, n: int, op: Callable[[T, T], T], e: T):
        self.root = SegtreeNode(0, e)
        self.n = n
        self.op = op
        self.e = e

    def _update(self, cur: SegtreeNode) -> None:
        l, r, op = cur.l, cur.r, self.op
        res = cur.value
        if l is not None:
            res = op(l.product, res)
        if r is not None:
            res = op(res, r.product)
        cur.product = res

    def _set(self, cur: SegtreeNode, a: int, b: int, i: int, value: T) -> None:
        if cur is None:
            cur = SegtreeNode(i, value)
            return
        if cur.idx == i:
            cur.value = value
            self._update(cur)
            return
        c = (a + b) >> 1
        if i < c:
            if cur.idx < i:
                cur.idx, i = i, cur.idx
                cur.value, value = value, cur.value
            if cur.l is None:
                cur.l = SegtreeNode(i, value)
            self._set(cur.l, a, c, i, value)
        else:
            if i < cur.idx:
                i, cur.idx = cur.idx, i
                cur.value, value = value, cur.value
            if cur.r is None:
                cur.r = SegtreeNode(i, value)
            self._set(cur.r, c, b, i, value)
        self._update(cur)
        return

    def _get(self, cur: SegtreeNode, a: int, b: int, i: int) -> T:
        if cur is None:
            return self.e
        if cur.idx == i:
            return cur.value
        c = (a + b) >> 1
        if i < c:
            return self._get(cur.l, a, c, i)
        else:
            return self._get(cur.r, c, b, i)

    def _prod(self, cur: SegtreeNode, a: int, b: int, l: int, r: int) -> T:
        if cur is None or b <= l or r <= a:
            return self.e
        if l <= a and b <= r:
            return cur.product
        c = (a + b) >> 1
        res = self._prod(cur.l, a, c, l, r)
        if l <= cur.idx and cur.idx < r:
            res = self.op(res, cur.value)
        return self.op(res, self._prod(cur.r, c, b, l, r))

    def set(self, i: int, value: T) -> None:
        self._set(self.root, 0, self.n, i, value)

    __setitem__ = set

    def get(self, i: int) -> T:
        self._get(self.root, 0, self.n, i)

    __getitem__ = get

    def prod(self, l: int, r: int) -> T:
        assert 0 <= l <= r and r <= self.n
        return self._prod(self.root, 0, self.n, l, r)

    def all_prod(self) -> T:
        return self.root.product if self.root else self.e
