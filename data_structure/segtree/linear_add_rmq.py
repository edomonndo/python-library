from typing import TypeVar

T = TypeVar("T")

from utility.bit import Bit32


class LinearAddRmQ:

    class Node:
        def __init__(self, x: int = 0, y: T = 0):
            self.lza = self.lzb = 0
            self.lbrx = self.rbrx = x
            self.lbry = self.rbry = y

        def __repr__(self):
            return f"Node<({self.lza},{self.lzb}),({self.lbrx},{self.lbry}),({self.rbrx},{self.rbry})>"

    def __init__(self, V: list[T]):
        self.n = len(V)
        self.op = min
        self.e = float("inf")
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.correct = [1] * (self.size << 1)
        self.d = [self.Node() for _ in range(self.size << 1)]
        for i in range(self.n):
            self.d[self.size + i] = self.Node(i, V[i])
        for i in range(self.n, self.size):
            self.d[self.size + i] = self.Node(i, 0)
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    @staticmethod
    def _cross(ax: int, ay: T, bx: int, by: T, cx: int, cy: T) -> T:
        return (by - ay) * (cx - ax) - (cy - ay) * (bx - ax)

    def set(self, p: int, x: T) -> None:
        assert 0 <= p and p < self.n
        p_orgin = p
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        if self.d[p].lbry == x:
            return
        is_decrease = self.d[p].lbry > x
        self.d[p] = self.Node(p_orgin, x)
        for i in range(1, self.log + 1):
            if (
                is_decrease
                or self.d[p >> i].lbrx == p_orgin
                or self.d[p >> i].rbrx == p_orgin
            ):
                self._update(p >> i)

    def get(self, p: int) -> T:
        assert 0 <= p and p < self.n
        p += self.size
        nd = self.d[p]
        a = nd.lza * self.log
        b = nd.lzb * self.log
        return nd.lbry + (p - self.size) * a + b

    def prod(self, l: int, r: int) -> T:
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        res = self.e
        while l < r:
            if l & 1:
                res = self.op(res, self._min_subtree(l))
                l += 1
            if r & 1:
                r -= 1
                res = self.op(self._min_subtree(r), res)
            l >>= 1
            r >>= 1
        return res

    def apply(self, l: int, r: int, a: T, b: T) -> None:
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        l2, r2 = l, r
        while l < r:
            if l & 1:
                self._all_apply(l, a, b)
                l += 1
            if r & 1:
                r -= 1
                self._all_apply(r, a, b)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.correct[l >> i] = 0
            if ((r >> i) << i) != r:
                self.correct[(r - 1) >> i] = 0

    def _leftmost(self, k: int) -> int:
        msb = 31 - Bit32.clz(k)
        return (k - (1 << msb)) << (self.log - msb)

    def _update(self, k: int) -> None:
        # assert 0 <= k < self.size
        correct, d, size = self.correct, self.d, self.size
        self._push(k)
        l, r = k << 1, (k << 1) + 1
        if not correct[l]:
            self._update(l)
        if not correct[r]:
            self._update(r)
        splitx = self._leftmost(r)
        lza = lzb = lzA = lzB = 0
        ax, ay = d[l].lbrx, d[l].lbry
        bx, by = d[l].rbrx, d[l].rbry
        cx, cy = d[r].lbrx, d[r].lbry
        dx, dy = d[r].rbrx, d[r].rbry

        def movel(f: int):
            nonlocal lza, lzb, l, ax, ay, bx, by
            lza += d[l].lza
            lzb += d[l].lzb
            l = (l << 1) + f
            ax, ay = d[l].lbrx, d[l].lbry
            bx, by = d[l].rbrx, d[l].rbry
            ay += lza * ax + lzb
            by += lza * bx + lzb

        def mover(f: int):
            nonlocal lzA, lzB, r, cx, cy, dx, dy
            lzA += d[r].lza
            lzB += d[r].lzb
            r = (r << 1) + f
            cx, cy = d[r].lbrx, d[r].lbry
            dx, dy = d[r].rbrx, d[r].rbry
            cy += lzA * cx + lzB
            dy += lzA * dx + lzB

        while l < size or r < size:
            s1 = self._cross(ax, ay, bx, by, cx, cy)
            if l < size and s1 > 0:
                movel(0)
            elif r < size and self._cross(bx, by, cx, cy, dx, dy) > 0:
                mover(1)
            elif l >= size:
                mover(0)
            elif r >= size:
                movel(1)
            else:
                s2 = self._cross(bx, by, ax, ay, dx, dy)
                if s1 + s2 == 0 or s1 * (dx - splitx) < s2 * (splitx - cx):
                    movel(1)
                else:
                    mover(0)
        d[k].lbrx, d[k].lbry = ax, ay
        d[k].rbrx, d[k].rbry = cx, cy
        correct[k] = 1

    def _all_apply(self, k: int, a: T, b: T) -> None:
        nd = self.d[k]
        nd.lbry += a * nd.lbrx + b
        nd.rbry += a * nd.rbrx + b
        if k < self.size:
            nd.lza += a
            nd.lzb += b

    def _push(self, k: int) -> None:
        nd = self.d[k]
        self._all_apply(k << 1, nd.lza, nd.lzb)
        self._all_apply((k << 1) + 1, nd.lza, nd.lzb)
        nd.lza = nd.lzb = 0

    def _min_subtree(self, k: int, a: T = 0, b: T = 0) -> T:
        d = self.d
        if not self.correct[k]:
            self._update(k)
        while k < self.size:
            f = (d[k].lbry - d[k].rbry) > a * (d[k].rbrx - d[k].lbrx)
            a += d[k].lza
            b += d[k].lzb
            k = (k << 1) + f
        return d[k].lbry + a * d[k].lbrx + b
