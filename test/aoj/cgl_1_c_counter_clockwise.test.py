# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_C

from geometory.geometory import Point

x1, y1, x2, y2 = map(int, input().split())
p0 = Point(x1, y1)
p1 = Point(x2, y2)

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    p2 = Point(x, y)
    res = p0.ccw(p1, p2)
    if res == 1:
        print("COUNTER_CLOCKWISE")
    elif res == -1:
        print("CLOCKWISE")
    elif res == 2:
        print("ONLINE_BACK")
    elif res == -2:
        print("ONLINE_FRONT")
    else:
        print("ON_SEGMENT")
