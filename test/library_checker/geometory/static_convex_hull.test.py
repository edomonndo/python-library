# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_convex_hull

from geometory.basic.point import Point
from geometory.convex_full import convex_hull

T = int(input())
for _ in range(T):
    n = int(input())
    xy = list(set(tuple(map(int, input().split())) for _ in range(n)))
    res = convex_hull([Point(x, y) for x, y in xy])
    print(len(res))
    for x, y in res:
        print(x, y)
