# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product

from linear_algebra.matrix import Matrix

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]

A = Matrix(N, M, A)
B = Matrix(M, K, B)

C = A * B
print(C)
