# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E

from data_structure.lazy_segment_tree import LazySegtree

N, Q = map(int, input().split())
INF = (1 << 31) - 1
A = [INF] * N
ID = float("inf")
G = LazySegtree(
    A, min, ID, lambda f, x: x if f == ID else f, lambda f, g: g if f == ID else f, ID
)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        G.apply(s, t + 1, x)
    else:
        s, t = q
        print(G.prod(s, t + 1))
