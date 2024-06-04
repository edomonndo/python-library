# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum

from geometory.offline_rectangle_add_rectangle_sum import (
    OfflineRectangleAddRectangleSum,
)

n, q = map(int, input().split())
solver = OfflineRectangleAddRectangleSum()
for _ in range(n):
    l, d, r, u, w = map(int, input().split())
    solver.add_rect(l, d, r, u, w)
for _ in range(q):
    l, d, r, u = map(int, input().split())
    solver.add_query(l, d, r, u)
print(*solver.solve(), sep="\n")
