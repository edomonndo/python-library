# verification-helper: PROBLEM https://judge.yosupo.jp/problem/division_of_polynomials
from polynomial.formal_power_series import FPS

n, m = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
q, r = FPS.divmod(A, B)
print(len(q), len(r))
print(*q)
print(*r)
