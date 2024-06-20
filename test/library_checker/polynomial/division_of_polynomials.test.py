# verification-helper: PROBLEM https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series
from convolution.formal_power_series import FPS

n, m = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
q, r = FPS.divmod(A, B)
print(len(q), len(r))
print(*q)
print(*r)
