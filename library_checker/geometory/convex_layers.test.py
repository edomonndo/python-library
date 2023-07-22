# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convex_layers

from geometory.convex_layers import convex_layers

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

ans = convex_layers(A)
print(*ans, sep="\n")
