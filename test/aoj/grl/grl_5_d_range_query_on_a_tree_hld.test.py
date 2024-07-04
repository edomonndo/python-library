# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D

from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition


def f(l, r):
    bit.add(l, w)


def g(l, r):
    global ans
    ans += bit.sum(l, r)


n = int(input())
edges = []
par = [-1] * n
for v in range(n):
    k, *us = map(int, input().split())
    for u in us:
        edges.append((v, u))
        par[u] = v
T = HeavyLightDecomposition(n, edges)
bit = FenwickTree(n)
q = int(input())
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        v, w = qu
        T.path_query(par[v], v, f, True)
    else:
        u = qu[0]
        ans = 0
        T.path_query(0, u, g, True)
        print(ans)
