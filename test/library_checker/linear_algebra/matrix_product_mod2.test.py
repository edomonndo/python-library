# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product_mod_2

# import sys
# sys.set_int_max_str_digits(0)

from linear_algebra.bit_matrix import BitMatrix


n, m, k = map(int, input().split())
A = BitMatrix.from_input(n, m)
B = BitMatrix.from_input(m, k)
C = A * B
print(C.tostr())
