# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite

from graph.tree.template import Tree
from data_structure.segtree.segment_tree import Segtree
from graph.tree.heavy_light_decomposition import HLD

MOD = 998244353
msk = (1 << 32) - 1


def op1(x, y):
    x1, x2 = x >> 32, x & msk
    y1, y2 = y >> 32, y & msk
    z1 = x1 * y1 % MOD
    z2 = (x2 * y1 % MOD + y2) % MOD
    return (z1 << 32) + z2


def op2(x, y):
    return op1(y, x)


n, q = map(int, input().split())
A = [0] * n
B = [0] * n
for i in range(n):
    A[i], B[i] = map(int, input().split())
g = Tree.from_input(n, 0)
hld = HLD(n, g)
P = hld.build_list([A[i] << 32 | B[i] for i in range(n)])
e = 1 << 32
seg1 = Segtree(P, op1, e)
seg2 = Segtree(P, op2, e)

for _ in range(q):
    t, a, b, c = map(int, input().split())
    if t == 0:
        p = hld.index(a)
        seg1.set(p, (b << 32) + c)
        seg2.set(p, (b << 32) + c)
    else:
        path = hld.path_query_noncommutative(a, b, False)
        res = e
        for l, r, is_rev in path:
            if is_rev:
                res = op1(res, seg2.prod(l, r))
            else:
                res = op1(res, seg1.prod(l, r))
        s, t = res >> 32, res & msk
        ans = (s * c % MOD + t) % MOD
        print(ans)
