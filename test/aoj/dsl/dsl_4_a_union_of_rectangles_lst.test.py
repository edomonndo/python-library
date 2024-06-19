# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A

from geometory.union_area_rectangle import union_area

n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]
print(union_area(rects))
