# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E

from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.fenwick_tree.range_add_range_sum import RangeAddRangeSum

n = int(input())
g = [[] for _ in range(n)]
par = [-1] * n
for v in range(n):
    k, *us = map(int, input().split())
    for u in us:
        g[u].append(v)
        g[v].append(u)
        par[u] = v
hld = HeavyLightDecomposition(n, g, 0, 0)
seg = RangeAddRangeSum([0] * n)
q = int(input())
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        v, w = qu
        for l, r in hld.path_query(par[v], v, True):
            seg.add(l, r, w)
    else:
        u = qu[0]
        ans = 0
        for l, r in hld.path_query(0, u, True):
            ans += seg.sum(l, r)
        print(ans)
