# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank_mod_2

import sys

input = sys.stdin.readline().rstrip
# sys.set_int_max_str_digits(0)

from linear_algebra.bit_matrix import BitMatrix


n, m = map(int, input().split())
A = BitMatrix.from_input(n, m)
print(A.rank())
