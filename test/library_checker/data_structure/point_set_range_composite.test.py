# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite

from data_structure.basic.segment_tree import Segtree

MOD = 998244353
mask = (1 << 30) - 1


def op(x, y):
    a, b = x >> 30, x & mask
    c, d = y >> 30, y & mask
    e, f = a * c % MOD, (c * b + d) % MOD
    return e << 30 | f


e = 1 << 30

N, Q = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]
g = Segtree([a << 30 | b for a, b in A], op, e)
for _ in range(Q):
    t, l, r, x = map(int, input().split())
    if t == 0:
        g.set(l, r << 30 | x)
    else:
        ab = g.prod(l, r)
        a, b = ab >> 30, ab & mask
        print((a * x + b) % MOD)
