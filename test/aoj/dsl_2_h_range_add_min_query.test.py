# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_H

from data_structure.segtree.lazy_segment_tree import LazySegtree

N, Q = map(int, input().split())
A = [0] * N
INF = float("inf")
G = LazySegtree(A, min, INF, lambda f, x: f + x, lambda f, g: f + g, 0)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        G.apply(s, t + 1, x)
    else:
        s, t = q
        print(G.prod(s, t + 1))
