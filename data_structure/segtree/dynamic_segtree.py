from typing import TypeVar, Callable

T = TypeVar("T")


class SegtreeNode:
    def __init__(self, i, value: T):
        self.idx = i
        self.value = value
        self.product = value
        self.p = None
        self.l = None
        self.r = None


class DynamicSegtree:
    def __init__(self, n: int, op: Callable[[T, T], T], e: T):
        self.root = SegtreeNode(0, e)
        self.n = n
        self.op = op
        self.e = e

    def _update(self, cur: SegtreeNode):
        l, r, op = cur.l, cur.r, self.op
        res = cur.value
        if l is not None:
            res = op(l.product, res)
        if r is not None:
            res = op(res, r.product)
        cur.product = res

    def set(self, i: int, value: T) -> None:
        assert 0 <= i < self.n
        stack = [(self.root, ~0, self.n), (self.root, 0, self.n)]
        while stack:
            cur, l, r = stack.pop()
            if l >= 0:
                if cur is None:
                    cur = SegtreeNode(i, value)
                    continue
                if cur.idx == i:
                    cur.value = value
                    continue
                m = (l + r) >> 1
                if i < m:
                    if cur.idx < i:
                        cur.idx, i = i, cur.idx
                        cur.value, value = value, cur.value
                    if cur.l is None:
                        cur.l = SegtreeNode(i, value)
                    stack += [(cur.l, ~l, m), (cur.l, l, m)]
                else:
                    if i < cur.idx:
                        i, cur.idx = cur.idx, i
                        cur.value, value = value, cur.value
                    if cur.r is None:
                        cur.r = SegtreeNode(i, value)
                    stack += [(cur.r, ~m, r), (cur.r, m, r)]
            else:
                self._update(cur)
        return

    __setitem__ = set

    def get(self, i: int) -> T:
        assert 0 <= i < self.n
        stack = [(self.root, 0, self.n)]
        while stack:
            cur, l, r = stack.pop()
            if cur is None:
                return self.e
            if cur.idx == i:
                return cur.value
            m = (l + r) >> 1
            if i < m:
                stack.append((cur.l, l, m))
            else:
                stack.append((cur.r, m, r))

    __getitem__ = get

    def prod(self, l: int, r: int) -> T:
        assert 0 <= l < r and r <= self.n
        stack = [(self.root, 0, self.n)]
        res = self.e
        while stack:
            cur, a, b = stack.pop()
            if cur is None or b <= l or r <= a:
                continue
            if l <= a and b <= r:
                res = self.op(res, cur.product)
                continue
            if l <= cur.idx < r:
                res = self.op(res, cur.value)
            c = (a + b) >> 1
            stack += [(cur.l, a, c), (cur.r, c, b)]
        return res

    def all_prod(self):
        return self.root.product if self.root else self.e
