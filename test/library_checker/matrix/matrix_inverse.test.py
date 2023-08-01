# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix

from matrix.matrix import Matrix

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A = Matrix(N, N, A)
print(A.inverse())
