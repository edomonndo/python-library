# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_A

from geometory.geometory import Point, Line

x1, y1, x2, y2 = map(int, input().split())
line = Line(Point(x1, y1), Point(x2, y2))

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    p = Point(x, y)
    ans = line.project(p)
    print(ans.x, ans.y)
