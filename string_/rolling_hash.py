class RollingHash:
    class FenwickTree:
        def __init__(self, n: int):
            self.n = n
            self.data = [0] * n

        def add(self, p: int, x: int):
            assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
            p += 1
            while p <= self.n:
                self.data[p - 1] += x
                p += p & -p

        def sum(self, l, r):
            assert (
                0 <= l and l <= r and r <= self.n
            ), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
            return self.sum0(r) - self.sum0(l)

        def sum0(self, r):
            s = 0
            while r > 0:
                s += self.data[r - 1]
                r -= r & -r
            return s

    def __init__(self, s: list[int], mod: int = 10**9 + 7, base: int = None):
        if base is None:
            import random

            base = random.randrange(2, mod)
        n = len(s)
        self.mod = mod
        self.power = [1] * (n + 1)
        v = 1
        for i in range(n):
            v = v * base % mod
            self.power[i + 1] = v

        self.hash = self.FenwickTree(n)
        self.value = [0] * n
        for i in range(n):
            v = self.power[i] * s[i] % self.mod
            self.hash.add(i, v)
            self.value[i] = v

    def update(self, p: int, x: int):
        v = self.power[p] * x % self.mod
        self.hash.add(p, (-self.value[p] + v) % self.mod)
        self.value[p] = v

    def get(self, l, r):
        return self.hash.sum(l, r) * self.power[-l - 1] % self.mod
