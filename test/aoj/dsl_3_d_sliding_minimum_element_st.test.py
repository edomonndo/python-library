# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D

from data_structure.sparse_table import SparseTable

N, L = map(int, input().split())
A = [int(x) for x in input().split()]
ST = SparseTable(A, min)
ans = []
for i in range(N + 1 - L):
    ans.append(ST.query(i, i + L))
print(*ans)
