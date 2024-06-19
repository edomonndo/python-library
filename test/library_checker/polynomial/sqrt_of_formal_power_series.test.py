# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
from convolution.formal_power_series import FPS

n = int(input())
A = [int(x) for x in input().split()]
ans = FPS.sqrt(A)
if ans:
    print(*ans)
else:
    print(-1)
