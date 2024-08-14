# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc

from graph.scc_incremental import incremental_scc
from graph.connectivity.unionfind import UnionFind

MOD = 998244353

n, m = map(int, input().split())
X = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(m)]
time = incremental_scc(n, edges)
ids = [[] for _ in range(m + 1)]
for ei in range(m):
    if time[ei] <= m:
        ids[time[ei]].append(ei)

uf = UnionFind(n)
ans = 0
for t in range(1, m + 1):
    for ei in ids[t]:
        u, v = edges[ei]
        u, v = uf.leader(u), uf.leader(v)
        if u == v:
            continue
        ans += X[u] * X[v] % MOD
        ans %= MOD
        uf.merge(u, v)
        X[uf.leader(u)] = (X[u] + X[v]) % MOD
    print(ans)
