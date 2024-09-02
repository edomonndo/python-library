# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D

from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from graph.tree.heavy_light_decomposition import HLD

n = int(input())
g = [[] for _ in range(n)]
par = [-1] * n
for v in range(n):
    k, *us = map(int, input().split())
    for u in us:
        g[v].append(u)
        par[u] = v
hld = HLD(n, g, is_undirect=False)
bit = FenwickTree(n)
q = int(input())
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        v, w = qu
        for l, r in hld.path_query(par[v], v, True):
            bit.add(l, w)
    else:
        u = qu[0]
        ans = 0
        for l, r in hld.path_query(0, u, True):
            ans += bit.sum(l, r)
        print(ans)
