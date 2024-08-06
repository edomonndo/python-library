# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_A

from geometory.basic.point import Point
from geometory.basic.polygon import Polygon

n = int(input())
ps = []
for i in range(n):
    x, y = map(float, input().split())
    ps.append(Point(x, y))
pol = Polygon(ps)
print(pol.area())
