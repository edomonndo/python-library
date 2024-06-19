# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D

from data_structure.segtree.dual_segment_tree import DualSegtree

N, Q = map(int, input().split())
INF = (1 << 31) - 1
A = [INF] * N
ID = float("inf")
G = DualSegtree(
    A, lambda f, x: x if f == ID else f, lambda f, g: g if f == ID else f, ID
)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        G.apply(s, t + 1, x)
    else:
        x = q[0]
        print(G.get(x))
