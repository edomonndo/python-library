# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum

from tree.euler_tour import EulerTour
from data_structure.segment_tree import Segtree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i, p in enumerate(P, 1):
    G[i].append((1, p))
    G[p].append((1, i))

et = EulerTour(N, G, 0, A)
seg = Segtree(et.vcost_st, (lambda x, y: x + y), 0)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        u, x = q
        cur = seg.get(u)
        seg.set(u, cur + x)
    elif t == 1:
        u = q[0]
        print(seg.prod(et.into[u], et.out[u]))
