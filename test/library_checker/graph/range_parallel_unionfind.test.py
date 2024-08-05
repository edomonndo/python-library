# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_parallel_unionfind

from graph.connectivity.unionfind import UnionFind
from graph.connectivity.range_parallel_unionfind import RangeParallelUnionFind

MOD = 998244353

n, q = map(int, input().split())
X = [int(x) for x in input().split()]
rpuf = RangeParallelUnionFind(n)
uf = UnionFind(n)
ans = 0
for i in range(q):
    k, a, b = map(int, input().split())
    if k != 0 and a != b:
        for u, v in rpuf.enumerate(a, b, k):
            u = uf.leader(u)
            v = uf.leader(v)
            w = uf.merge(u, v)
            ans += X[u] * X[v] % MOD
            ans %= MOD
            X[w] = X[u] + X[v]
    print(ans)
