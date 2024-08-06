# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_C

from geometory.basic.point import Point
from geometory.basic.polygon import Polygon

n = int(input())
ps = []
for i in range(n):
    x, y = map(float, input().split())
    ps.append(Point(x, y))
pol = Polygon(ps)
q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(pol.contains(Point(x, y)))
