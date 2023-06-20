# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix

from matrix.matrix import Matrix

N = int(input())
A = list(map(int, input().split()))

A = Matrix(N, N, A)
print(A.inverse())
