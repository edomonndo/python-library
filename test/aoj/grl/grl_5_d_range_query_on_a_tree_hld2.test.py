# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D

from graph.tree.hld_segtree import HldSegTree

n = int(input())
edges = []
par = [-1] * n
for v in range(n):
    k, *us = map(int, input().split())
    for u in us:
        edges.append((v, u))
        par[u] = v
seg = HldSegTree(lambda x, y: x + y, 0, [0] * n, n, edges)
q = int(input())
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        v, w = qu
        seg.set(v, seg.get(v) + w)
    else:
        u = qu[0]
        print(seg.path_prod(0, u))
