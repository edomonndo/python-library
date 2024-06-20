# verification-helper: PROBLEM https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series
from convolution.composition import *

n = int(input())
A = [int(x) for x in input().split()]
print(*composition_inverse(A))
