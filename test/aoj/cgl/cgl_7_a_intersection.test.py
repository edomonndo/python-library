# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_A

from geometory.basic.circle import Circle

x, y, r = map(int, input().split())
C1 = Circle.from_int(x, y, r)
x, y, r = map(int, input().split())
C2 = Circle.from_int(x, y, r)
print(C1.intersect(C2))
