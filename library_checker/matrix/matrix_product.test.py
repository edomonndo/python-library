# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product

from matrix.matrix import Matrix

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = Matrix(N, M, A)
B = Matrix(M, K, B)

C = A * B
for row in C:
    print(*row)
