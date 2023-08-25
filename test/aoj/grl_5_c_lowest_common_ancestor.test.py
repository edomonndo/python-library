# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C

from tree.euler_tour import EulerTour
from data_structure.segment_tree import Segtree

N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    k, *es = map(int, input().split())
    for e in es:
        G[i].append((1, e))
        G[e].append((1, i))

et = EulerTour(N, G, 0, [0] * N)
seg = Segtree(et.depth, min, (10**9, -1))
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    if u == v:
        print(u)
        continue
    l, r = et.into[u], et.into[v]
    if l > r:
        l, r = r, l
    _, lca = seg.prod(l, r)
    if lca < 0:
        print(et.parent[~lca])
    else:
        print(lca)
