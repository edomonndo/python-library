# verification-helper: PROBLEM https://judge.yosupo.jp/problem/composition_of_formal_power_series
from polynomial.composition import *

n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(*composition(A, B))
