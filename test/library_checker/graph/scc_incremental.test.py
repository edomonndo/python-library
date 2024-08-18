# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc

from collections import defaultdict

from graph.scc_incremental import incremental_scc
from graph.connectivity.unionfind import UnionFind

MOD = 998244353

n, m = map(int, input().split())
X = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(m)]
time = incremental_scc(n, edges)
ids = defaultdict(list)
for ei in range(m):
    if time[ei] <= m:
        ids[time[ei]].append(ei)

uf = UnionFind(n)
ans = [0] * m
for t in sorted(ids.keys()):
    for ei in ids[t]:
        u, v = edges[ei]
        u, v = uf.leader(u), uf.leader(v)
        if u == v:
            continue
        ans[t - 1] += X[u] * X[v] % MOD
        ans[t - 1] %= MOD
        uf.merge(u, v)
        X[uf.leader(u)] = (X[u] + X[v]) % MOD
for i in range(m - 1):
    ans[i + 1] = (ans[i + 1] + ans[i]) % MOD
print(*ans, sep="\n")
