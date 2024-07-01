# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det

from linear_algebra.matrix import Matrix

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A = Matrix(N, N, A)
print(A.determinant())
