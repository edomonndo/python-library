# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E

from data_structure.dual_segment_tree import DualSegtree

N, Q = map(int, input().split())
A = [0] * N
G = DualSegtree(A, lambda f, x: f + x, lambda f, g: f + g, 0)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        G.apply(s - 1, t, x)
    else:
        x = q[0]
        print(G.get(x - 1))
