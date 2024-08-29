# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix_mod_2

# import sys
# sys.set_int_max_str_digits(0)

from linear_algebra.bit_matrix import BitMatrix


n = int(input())
A = BitMatrix.from_input(n, n)
A_inv = A.inv()
if A_inv:
    print(A_inv.tostr())
else:
    print(-1)
