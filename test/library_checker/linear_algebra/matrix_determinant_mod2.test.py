# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det_mod_2

# import sys
# sys.set_int_max_str_digits(0)

from linear_algebra.bit_matrix import BitMatrix


n = int(input())
A = BitMatrix.from_input(n, n)
print(A.det())
