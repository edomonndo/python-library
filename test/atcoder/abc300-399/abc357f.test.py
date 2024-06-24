# verification-helper: PROBLEM https://atcoder.jp/contests/abc339/tasks/abc339_g

from data_structure.segtree.monoids_action.range_add_range_product_sum import *
from atcoder.lazysegtree import LazySegTree

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
seg = LazySegTree(
    op,
    S(0, 0, 0, 0),
    mapping,
    composition,
    F(0, 0),
    [S(a, b, a * b, 1) for a, b in zip(A, B)],
)
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 3:
        l, r = qu
        print(seg.prod(l - 1, r).ab)
    else:
        l, r, x = qu
        f = F(x, 0) if t == 1 else F(0, x)
        seg.apply(l - 1, r, f)
