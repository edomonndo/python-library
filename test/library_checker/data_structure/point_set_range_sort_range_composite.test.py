# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite

from data_structure.segtree.sortable_segtree import SortableSegtree

MOD = 998244353
mask = (1 << 30) - 1


def op(x, y):
    x1, x2, x3 = x[0], x[1] >> 30, x[1] & mask
    y1, y2, y3 = y[0], y[1] >> 30, y[1] & mask
    return (
        x1 * y1 % MOD,
        ((y1 * x2 % MOD + y2) % MOD) << 30 | (x1 * y3 % MOD + x3) % MOD,
    )


e_ = (1, 0)


def toggle(x):
    x1, x2 = x
    return (x1, (x2 & mask) << 30 | x2 >> 30)


n, q = map(int, input().split())
P = []
for _ in range(n):
    p, a, b = map(int, input().split())
    P.append((p, (a, b << 30 | b)))

seg = SortableSegtree(P)
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        i, p, a, b = qu
        seg.set(i, p, (a, b << 30 | b))
    elif t == 1:
        l, r, x = qu
        a, b = seg.prod(l, r)
        print((a * x + (b >> 30)) % MOD)
    else:
        l, r = qu
        seg.sort(l, r, t == 3)
