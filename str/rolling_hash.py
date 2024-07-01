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

    def __init__(
        self,
        s: list[int],
        L: int = 2,
        mods: tuple[int] = (10**9 + 7, 10**9 + 9),
        bases: tuple[int] = None,
    ):
        if bases is None:
            import random

            bases = [random.randrange(2, mod) for mod in mods]
        self.n = n = len(s)
        self.L = L
        self.mods = mods
        self.power = [[1] * (n + 1) for _ in range(L)]
        for i in range(L):
            v = 1
            for j in range(n):
                v = v * bases[i] % mods[i]
                self.power[i][j + 1] = v

        self.hashs = [self.FenwickTree(n) for _ in range(L)]
        self.values = [[0] * n for _ in range(L)]
        for i in range(L):
            for j in range(n):
                v = self.power[i][j] * s[j] % self.mods[i]
                self.hashs[i].add(j, v)
                self.values[i][j] = v

    def update(self, p: int, x: int):
        for i in range(self.L):
            v = self.power[i][p] * x % self.mods[i]
            self.hashs[i].add(p, (-self.values[i][p] + v) % self.mods[i])
            self.values[i][p] = v

    def get(self, l: int, r: int) -> tuple[int]:
        res = []
        for i in range(self.L):
            res.append(self.hashs[i].sum(l, r) * self.power[i][-l - 1] % self.mods[i])
        return tuple(res)

    def connect(self, h1: int, h2: int, h2len: int) -> tuple[int]:
        res = []
        for i in range(self.L):
            res.append((h1 * self.power[i][h2len] + h2) % self.mods[i])
        return tuple(res)

    def lcp(self, l, r) -> int:
        def _ok(length) -> bool:
            d = dict()
            for i in range(self.n - length + 1):
                h = self.get(i, i + length)
                if h in d:
                    if (i - d[h]) >= length:
                        return True
                else:
                    d[h] = i
            return False

        while (r - l) > 1:
            m = (r + l) >> 1
            if _ok(m):
                l = m
            else:
                r = m
        return l
