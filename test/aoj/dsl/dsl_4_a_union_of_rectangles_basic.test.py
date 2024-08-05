# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A

from geometory.basic.rectangle import Rectangle, Rectangles

N = int(input())
rects = Rectangles()
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    rects.add(Rectangle.from_int(x1, y1, x2, y2))
print(rects.area())
