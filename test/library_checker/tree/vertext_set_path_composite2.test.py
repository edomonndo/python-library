# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite

from graph.tree.hld_segtree_noncommutative import HldSegTree

MOD = 998244353
msk = (1 << 32) - 1


def op(x, y):
    x1, x2 = x >> 32, x & msk
    y1, y2 = y >> 32, y & msk
    z1 = x1 * y1 % MOD
    z2 = (x2 * y1 % MOD + y2) % MOD
    return (z1 << 32) + z2


n, q = map(int, input().split())
A = [0] * n
B = [0] * n
for i in range(n):
    A[i], B[i] = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
V = [None] * n
for i, (a, b) in enumerate(zip(A, B)):
    V[i] = (a << 32) + b

seg = HldSegTree(op, 1 << 32, V, n, edges, 0)
for _ in range(q):
    t, a, b, c = map(int, input().split())
    if t == 0:
        seg.set(a, (b << 32) + c)
    else:
        res = seg.prod(a, b)
        a, b = res >> 32, res & msk
        print((a * c + b) % MOD)
