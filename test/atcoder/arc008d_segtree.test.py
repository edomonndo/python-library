# verification-helper: IGNORE https://atcoder.jp/contests/arc008/tasks/arc008_4

from data_structure.compressed_segtree import CompressedSegtree


def op(x, y):
    a, b = x
    c, d = y
    return (a * c, b * c + d)


e = (1, 0)

n, m = map(int, input().split())
A = []
Ps = dict()
for i in range(m):
    p, a, b = input().split()
    p = int(p) - 1
    a = float(a)
    b = float(b)
    A.append((p, a, b))
    Ps[p] = (1, 0)

mx = 1
mn = 1
seg = CompressedSegtree(op, e, Ps)
for p, a, b in A:
    seg[p] = (a, b)
    a, b = seg.all_prod()
    x = a + b
    mx = max(mx, x)
    mn = min(mn, x)
print(mn)
print(mx)
