from typing import TypeVar

T = TypeVar("T")


class FenwickTree:
    def __init__(self, N: int, e: T = 0):
        self.n = N
        self.data = [e for i in range(N)]
        self.e = e

    def add(self, p: int, x: T) -> None:
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while p <= self.n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l: int, r: int) -> T:
        assert 0 <= l and l <= r and r <= self.n, "0<=l<=r<=n,l={0},r={1},n={2}".format(
            l, r, self.n
        )
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r: int) -> T:
        s = self.e
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def bisect_left(self, x: T) -> int:
        """minimize i s.t. sum[0, i) >= x. Note x should be integer."""

        if x <= self.e:
            return 0
        p = 0
        k = 1 << (self.n.bit_length() - 1)
        while k:
            if p + k <= self.n and self.data[p + k - 1] < x:
                x -= self.data[p + k - 1]
                p += k
            k >>= 1
        return p + 1

    def bisect_right(self, x: T) -> int:
        """minimize i s.t. sum[0,i) > x. Note x should be integer."""
        if x <= self.e:
            return 0
        p = 0
        k = 1 << (self.n.bit_length() - 1)
        while k:
            if p + k <= self.n and self.data[p + k - 1] <= x:
                x -= self.data[p + k - 1]
                p += k
            k >>= 1
        return p + 1
