# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_point_get

from data_structure.segtree.dual_segment_tree import DualSegtree

MOD = 998244353
mask = (1 << 30) - 1
ID = 1 << 30


def mapping(F, x):
    a, b = F >> 30, F & mask
    c, d = x >> 30, x & mask
    e, f = (a * c + b * d) % MOD, d
    return e << 30 | f


def composition(F, G):
    a, b = F >> 30, F & mask
    c, d = G >> 30, G & mask
    e, f = a * c % MOD, (a * d + b) % MOD
    return e << 30 | f


N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
g = DualSegtree([(a << 30) | 1 for a in A], mapping, composition, ID)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        l, r, b, c = q
        g.apply(l, r, b << 30 | c)
    else:
        i = q[0]
        ab = g.get(i)
        a, b = ab >> 30, ab & mask
        print(a)
