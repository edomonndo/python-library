# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_B

from geometory.basic.line import Line

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    l1 = Line.from_int(x1, y1, x2, y2)
    l2 = Line.from_int(x3, y3, x4, y4)
    if l1.intersect(l2):
        print(1)
    else:
        print(0)
