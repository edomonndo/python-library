# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group

from graph.connectivity.weighted_union_find import WeightedUnionFind

MOD = 998244353


class Monoid:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"M<{self.a},{self.b},{self.c},{self.d}>"

    __repr__ = __str__

    def __add__(self, other: "Monoid") -> "Monoid":
        ds = [[self.a, self.b], [self.c, self.d]]
        do = [[other.a, other.b], [other.c, other.d]]
        dat = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    dat[i][k] += do[i][j] * ds[j][k]
                    dat[i][k] %= MOD
        return Monoid(dat[0][0], dat[0][1], dat[1][0], dat[1][1])

    def __neg__(self) -> "Monoid":
        return Monoid(self.d, -self.b % MOD, -self.c % MOD, self.a)

    def __sub__(self, other: "Monoid") -> "Monoid":
        return self + other.__neg__()

    def ok(self, other: "Monoid") -> bool:
        if (
            self.a == other.a
            and self.b == other.b
            and self.c == other.c
            and self.d == other.d
        ):
            return True
        return False

    def to_list(self) -> list[int]:
        return [self.a, self.b, self.c, self.d]


n, q = map(int, input().split())
uf = WeightedUnionFind(n, Monoid(1, 0, 0, 1))
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        u, v, a, b, c, d = qu
        p = Monoid(a, b, c, d)
        if uf.same(u, v):
            x = uf.diff(u, v)
            if x.ok(p):
                print(1)
            else:
                print(0)

        else:
            uf.merge(u, v, p)
            print(1)
    else:
        u, v = qu
        if uf.same(u, v):
            x = uf.diff(u, v)
            print(*x.to_list())
        else:
            print(-1)
