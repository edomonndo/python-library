# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_convex_hull

from geometory.convex_full import convex_hull

T = int(input())
for _ in range(T):
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    res = convex_hull(xy)
    print(len(res))
    for x, y in res:
        print(x, y)
