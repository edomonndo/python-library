# verification-helper: IGNORE https://atcoder.jp/contests/arc008/tasks/arc008_4

from data_structure.dynamic_segtree import DynamicSegtree


def op(x, y):
    a, b = x
    c, d = y
    return (a * c, b * c + d)


e = (1, 0)

n, m = map(int, input().split())
seg = DynamicSegtree(n, op, e)
inf = float("inf")
mx = 1
mn = 1
for i in range(m):
    p, a, b = input().split()
    seg[int(p) - 1] = (float(a), float(b))
    a, b = seg.all_prod()
    x = a + b
    mx = max(mx, x)
    mn = min(mn, x)

print(mn)
print(mx)
