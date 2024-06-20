# verification-helper: PROBLEM https://judge.yosupo.jp/problem/product_of_polynomial_sequence

from convolution.sample_point_shift import *


n, m, c = map(int, input().split())
f = [int(x) for x in input().split()]
print(*sample_point_shift(f, c, m))
