# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B

from data_structure.fenwick_tree.fenwick_tree import FenwickTree

N, Q = map(int, input().split())
FT = FenwickTree(N)

ans = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        FT.add(x - 1, y)
    else:
        ans.append(FT.sum(x - 1, y))
print(*ans, sep="\n")
