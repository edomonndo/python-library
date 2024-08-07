# verification-helper: PROBLEM https://atcoder.jp/contests/abc341/tasks/abc341_e

from data_structure.segtree.lazy_segment_tree import LazySegtree


def op(x, y):
    if x == -1:
        return y
    if y == -1:
        return x
    ok1, l1, r1 = x >> 2 & 1, x >> 1 & 1, x & 1
    ok2, l2, r2 = y >> 2 & 1, y >> 1 & 1, y & 1
    if ok1 and ok2 and r1 != l2:
        ok = 1
    else:
        ok = 0
    return ok << 2 | l1 << 1 | r2


def mapping(f: int, x):
    if f and x != -1:
        ok, l, r = x >> 2 & 1, x >> 1 & 1, x & 1
        l ^= 1
        r ^= 1
        return ok << 2 | l << 1 | r
    else:
        return x


def composition(g: int, f: int):
    return g ^ f


n, q = map(int, input().split())
S = [int(x) for x in input()]
g = LazySegtree(
    [1 << 2 | 1 << 1 | 1 if s else 1 << 2 for s in S], op, -1, mapping, composition, 0
)
for _ in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    if t == 1:
        g.apply(l, r, 1)
    else:
        res = g.prod(l, r)
        print("Yes" if (res >> 2) & 1 else "No")
