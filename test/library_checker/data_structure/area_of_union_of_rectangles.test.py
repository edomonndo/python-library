# verification-helper: PROBLEM https://judge.yosupo.jp/problem/area_of_union_of_rectangles

from geometory.union_area_rectangle import union_area

n = int(input())
rects = []
for _ in range(n):
    l, d, r, u = map(int, input().split())
    rects.append((l, d, r, u))
print(union_area(rects))
