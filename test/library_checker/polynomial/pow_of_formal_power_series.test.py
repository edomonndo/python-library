# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_formal_power_series
from convolution.formal_power_series import FPS

n, m = map(int, input().split())
A = [int(x) for x in input().split()]
print(*FPS.pow(A, m))
