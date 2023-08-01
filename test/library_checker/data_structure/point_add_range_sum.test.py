# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

from data_structure.fenwick_tree import FenwickTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

INF = 1 << 60
FT = FenwickTree(N)
for i, a in enumerate(A):
    FT.add(i, a)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        FT.add(x, y)
    elif t == 1:
        print(FT.sum(x, y))
