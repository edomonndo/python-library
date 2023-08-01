# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum

from data_structure.fenwick_tree import FenwickTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

FT = FenwickTree(N)
for i, a in enumerate(A):
    FT.add(i, a)

for _ in range(Q):
    l, r = map(int, input().split())
    print(FT.sum(l, r))
