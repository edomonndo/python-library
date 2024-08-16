# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_B
# verification-helper: ERROR 1e-6

from geometory.basic.circle import Circle

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
C = Circle.from_triangle(x1, y1, x2, y2, x3, y3)
print(C.center.x, C.center.y, C.r)
