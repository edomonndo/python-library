# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B

from geometory.basic.line import Line

x1, y1, x2, y2 = map(int, input().split())
line = Line.from_int(x1, y1, x2, y2)

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    ans = line.refrection(x, y)
    print("{:.10f}".format(ans.x), "{:.10f}".format(ans.y))
