# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det_arbitrary_mod

from matrix.determinant_arbitrary import determinant_arbitrary_mod

N, MOD = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

print(determinant_arbitrary_mod(N, A, MOD))
