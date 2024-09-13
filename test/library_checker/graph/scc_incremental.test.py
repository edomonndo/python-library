# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc

from utility.fastio import Fastio
from graph.scc_incremental import IncrementalScc
from graph.connectivity.unionfind import UnionFind

import sys

sys.setrecursionlimit(1_000_000)

MOD = 998244353

fastio = Fastio()
rd = fastio.read
wrtln = fastio.writeln


n, m = rd(), rd()
X = [rd() for _ in range(n)]
edges = []
scc = IncrementalScc(n)
for _ in range(m):
    u, v = rd(), rd()
    edges.append((u, v))
    scc.add_edge(u, v)
res = scc.solve()
uf = UnionFind(n)
ans = 0
for i in range(m):
    for ei in res[i]:
        u, v = edges[ei]
        u = uf.leader(u)
        v = uf.leader(v)
        w = uf.merge(u, v)
        ans = (X[u] * X[v] + ans) % MOD
        X[w] = X[u] + X[v]
        if X[w] >= MOD:
            X[w] -= MOD
    wrtln(ans)
