# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B

from data_structure.segtree.segtree_2d import Segtree2d

n = int(input())
seg = Segtree2d(1000, 1000, max, 0, [])
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    seg.set(x1, y1, seg.get(x1, y1) + 1)
    seg.set(x1, y2, seg.get(x1, y2) - 1)
    seg.set(x2, y1, seg.get(x2, y1) - 1)
    seg.set(x2, y2, seg.get(x2, y2) + 1)

ans = 0
for x in range(1000):
    for y in range(1000):
        ans = max(ans, seg.prod(0, 0, x + 1, y + 1))
print(ans)
