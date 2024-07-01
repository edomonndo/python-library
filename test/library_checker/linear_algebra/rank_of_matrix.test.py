# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank

from linear_algebra.matrix import Matrix

n, m = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(n)]
M = Matrix(n, m, A)
print(M.rank())
