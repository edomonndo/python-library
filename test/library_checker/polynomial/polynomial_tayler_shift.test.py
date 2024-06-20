# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_taylor_shift
from convolution.tayler_shift import *

n, c = map(int, input().split())
A = [int(x) for x in input().split()]
print(*tayler_shift(A, c))
