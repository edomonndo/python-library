# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_I

from data_structure.segtree.lazy_segment_tree import LazySegtree

N, Q = map(int, input().split())
A = [(0, 1)] * N
INF = float("inf")
G = LazySegtree(
    A,
    lambda x, y: (x[0] + y[0], x[1] + y[1]),
    (0, 1),
    lambda f, x: x if f == INF else (f * x[1], x[1]),
    lambda f, g: g if f == INF else f,
    INF,
)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        G.apply(s, t + 1, x)
    else:
        s, t = q
        print(G.prod(s, t + 1)[0])
