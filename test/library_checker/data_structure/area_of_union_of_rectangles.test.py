# verification-helper: PROBLEM https://judge.yosupo.jp/problem/area_of_union_of_rectangles

from geometory.geometory import Rectangles, Rectangle, Point

n = int(input())
rects = Rectangles()
for _ in range(n):
    l, d, r, u = map(int, input().split())
    rects.add(Rectangle(Point(l, d), Point(r, u)))
print(rects.union_area())
