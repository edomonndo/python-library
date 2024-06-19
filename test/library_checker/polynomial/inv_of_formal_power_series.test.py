# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inv_of_formal_power_series

from convolution.formal_power_series import FPS

n = int(input())
A = [int(x) for x in input().split()]
print(*FPS.inv(A))
