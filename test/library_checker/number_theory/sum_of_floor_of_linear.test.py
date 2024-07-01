# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear

from number_theory.floor_sum import floor_sum

T = int(input())
ans = [None] * T
for i in range(T):
    N, M, A, B = map(int, input().split())
    ans[i] = floor_sum(N, M, A, B)

print(*ans, sep="\n")
