# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_linear_add_range_min

from data_structure.segtree.linear_add_rmq import LinearAddRmQ

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
inf = float("inf")
seg = LinearAddRmQ(A)
for i in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        l, r, b, c = qu
        seg.apply(l, r, b, c)
    else:
        l, r = qu
        print(seg.prod(l, r))
