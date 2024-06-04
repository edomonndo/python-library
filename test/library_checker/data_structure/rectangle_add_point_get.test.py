# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_add_point_get

from geometory.offline_rectangle_add_point_get import OfflineRectangleAddPointGet


n, q = map(int, input().split())
solver = OfflineRectangleAddPointGet()
for _ in range(n):
    l, d, r, u, w = map(int, input().split())
    solver.add_rect(l, d, r, u, w)
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        l, d, r, u, w = qu
        solver.add_rect(l, d, r, u, w)
    else:
        x, y = qu
        solver.add_query(x, y)
print(*solver.solve(), sep="\n")
