# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E

from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.fenwick_tree.range_add_range_sum import RangeAddRangeSum


def f(l, r):
    seg.add(l, r, w)


def g(l, r):
    global ans
    ans += seg.sum(l, r)


n = int(input())
edges = []
for v in range(n):
    k, *us = map(int, input().split())
    for u in us:
        edges.append((v, u))
T = HeavyLightDecomposition(n, edges)
seg = RangeAddRangeSum([0] * n)
q = int(input())
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        v, w = qu
        T.path_query(0, v, f, True)
    else:
        u = qu[0]
        ans = 0
        T.path_query(0, u, g, True)
        print(ans)
