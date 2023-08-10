# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_B

from geometory.geometory import Point, Line

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    l1 = Line(Point(x1, y1), Point(x2, y2))
    l2 = Line(Point(x3, y3), Point(x4, y4))
    if l1.intersect(l2):
        print(1)
    else:
        print(0)
