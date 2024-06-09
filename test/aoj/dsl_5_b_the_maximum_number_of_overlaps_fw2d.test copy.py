# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B

from data_structure.fenwick_tree.dynamic_fenwick_tree_2d import DynamicFenwickTree2d

n = int(input())
fw = DynamicFenwickTree2d(1000, 1000, 0)
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    fw.add_rect(x1, y1, x2 - 1, y2 - 1, 1)

ans = 0
for x in range(1000):
    for y in range(1000):
        ans = max(ans, fw.sum0(x, y))
print(ans)
