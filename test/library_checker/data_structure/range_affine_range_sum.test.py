# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum
from data_structure.lazy_segment_tree import LazySegtree

MOD = 998244353
mask = (1 << 30) - 1
e = 0
ID = 1 << 30


def op(x, y):
    a, b = x >> 30, x & mask
    c, d = y >> 30, y & mask
    e, f = (a + c) % MOD, b + d
    return e << 30 | f


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
g = LazySegtree([(a << 30) | 1 for a in A], op, e, mapping, composition, ID)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        l, r, b, c = q
        g.apply(l, r, b << 30 | c)
    else:
        l, r = q
        ab = g.prod(l, r)
        a, b = ab >> 30, ab & mask
        print(a)
