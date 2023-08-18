# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G

from data_structure.lazy_segment_tree import LazySegtree

N, Q = map(int, input().split())
A = [(0, 1)] * N
INF = float("inf")
G = LazySegtree(
    A,
    lambda x, y: (x[0] + y[0], x[1] + y[1]),
    (0, 1),
    lambda f, x: (x[0] + f * x[1], x[1]),
    lambda f, g: f + g,
    0,
)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        G.apply(s - 1, t, x)
    else:
        s, t = q
        print(G.prod(s - 1, t)[0])
