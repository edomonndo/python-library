# verification-helper: PROBLEM https://yukicoder.me/problems/no/875


from data_structure.segtree.monoids.range_min_index import *
from atcoder.segtree import SegTree

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
seg = SegTree(op, S(), [S(A[i], i + 1) for i in range(n)])
for _ in range(q):
    t, l, r = map(int, input().split())
    if t == 1:
        l -= 1
        r -= 1
        tmp = seg.get(l)
        lv, li = tmp.value, tmp.index
        tmp = seg.get(r)
        rv, ri = tmp.value, tmp.index
        seg.set(l, S(rv, li))
        seg.set(r, S(lv, ri))
    else:
        l -= 1
        print(seg.prod(l, r).index)
