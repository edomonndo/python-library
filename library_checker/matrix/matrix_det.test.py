# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det

from matrix.matrix import Matrix

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = Matrix(N, M, A)
print(A.determinant())
