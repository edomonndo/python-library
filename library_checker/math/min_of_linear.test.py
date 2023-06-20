# verification-helper: PROBLEM https://judge.yosupo.jp/problem/min_of_mod_of_linear

from math.min_of_linear import min_of_linear

T = int(input())
ans = [None] * T
for i in range(T):
    N, M, A, B = map(int, input().split())
    _, ans[i] = min_of_linear(0, N, A, B, M)

print(*ans, sep="\n")
