# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convex_layers

from geometory.convex_layers import convex_hull

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

ans = convex_hull(A)
print(*ans, sep="\n")
