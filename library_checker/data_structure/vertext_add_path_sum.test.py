# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum

from tree.euler_tour import EulerTour
from data_structure.segment_tree import Segtree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append((1, v))
    G[v].append((1, u))

et = EulerTour(N, G, 0, A)
segPQ = Segtree(et.vcost, (lambda x, y: x + y), 0)
segLca = Segtree(et.depth, min, 10**9)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        p, x = q
        segPQ.set(p, x)
    elif t == 1:
        u, v = q
        l, r = et.into[u], et.into[v]
        if l > r:
            l, r = r, l
        lca = segLca.prod(l, r + 1)
        m = et.into[lca]
        print(
            segPQ.prod(0, l + 1)
            + segPQ.prod(0, r + 1)
            - 2 * segPQ.prod(0, m + 1)
            + segPQ.get(m)
        )
