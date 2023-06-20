# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det

from matrix.matrix import determinant_arbitrary_mod

N, M = map(int, input().split())
A = list(map(int, input().split()))

print(determinant_arbitrary_mod(N, A, M))
