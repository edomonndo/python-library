# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum
from geometory.offline_point_add_rectangle_sum import OfflinePointAddRectangleSum


n, q = map(int, input().split())
G = OfflinePointAddRectangleSum()
for _ in range(n):
    x, y, w = map(int, input().split())
    G.add_point(x, y, w)
for i in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        x, y, w = qu
        G.add_point(x, y, w)
    else:
        x1, y1, x2, y2 = qu
        G.add_query(x1, y1, x2, y2)

ans = G.solve()
print(*ans, sep="\n")
