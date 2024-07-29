# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential

from graph.connectivity.weighted_unionfind import WeightedUnionFind

MOD = 998244353


class Monoid:
    def __init__(self, val=0):
        self.val = val % MOD

    def __str__(self):
        return f"M<{self.val}>"

    __repr__ = __str__

    def __add__(self, other: "Monoid") -> "Monoid":
        return Monoid(self.val + other.val)

    def __neg__(self) -> "Monoid":
        return Monoid(-self.val)

    def __sub__(self, other: "Monoid") -> "Monoid":
        return self + other.__neg__()


n, q = map(int, input().split())
uf = WeightedUnionFind(n, Monoid(0))
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        u, v, x = qu
        if uf.same(u, v):
            if uf.diff(u, v).val == x:
                print(1)
            else:
                print(0)
        else:
            uf.merge(u, v, Monoid(x))
            print(1)
    else:
        u, v = qu
        res = uf.diff(u, v)
        if res:
            print(res.val)
        else:
            print(-1)
