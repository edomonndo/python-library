# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite

from atcoder.segtree import SegTree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition

MOD = 998244353
msk = (1 << 32) - 1


def op1(x, y):
    x1, x2 = x >> 32, x & msk
    y1, y2 = y >> 32, y & msk
    z1 = x1 * y1 % MOD
    z2 = (x2 * y1 % MOD + y2) % MOD
    return (z1 << 32) + z2


def op2(x, y):
    x1, x2 = x >> 32, x & msk
    y1, y2 = y >> 32, y & msk
    z1 = x1 * y1 % MOD
    z2 = (x1 * y2 % MOD + x2) % MOD
    return (z1 << 32) + z2


def f(x, y):
    global ans
    if x <= y:
        res = seg1.prod(x, y)
    else:
        res = seg2.prod(y, x)
    s, t = res >> 32, res & msk
    ans = (s * ans % MOD + t) % MOD


n, q = map(int, input().split())
A = [0] * n
B = [0] * n
for i in range(n):
    A[i], B[i] = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
H = HeavyLightDecomposition(n, edges, 0)
P = [None] * n
for h, a, b in zip(H.into, A, B):
    P[h] = (a << 32) + b

seg1 = SegTree(op1, 1 << 32, P)
seg2 = SegTree(op2, 1 << 32, P)

for _ in range(q):
    t, a, b, c = map(int, input().split())
    if t == 0:
        p = H.into[a]
        seg1.set(p, (b << 32) + c)
        seg2.set(p, (b << 32) + c)
    else:
        ans = c
        H.path_noncommutative_query(a, b, f)
        print(ans)
