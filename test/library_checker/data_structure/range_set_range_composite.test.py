# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_set_range_composite

from data_structure.range_set_range_composite import RangeSetRangeComposite

MOD = 998244353
mask = (1 << 30) - 1


def op(x, y):
    x0, x1 = x >> 30, x & mask
    y0, y1 = y >> 30, y & mask
    return (x0 * y0 % MOD) << 30 | (y0 * x1 + y1) % MOD


def pow_(x: int, y: int):
    x0, x1 = x >> 30, x & mask
    a = pow(x0, y, MOD)
    if x0 <= 1:
        b = y * x0 * x1 % MOD
    else:
        b = (a - 1) * pow(a - 1, -1, MOD) * x1 % MOD
    return a << 30 | b


n, q = map(int, input().split())
A = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a << 30 | b)
seg = RangeSetRangeComposite(op, 1 << 30, pow_, 1 << 30, A)
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        l, r, c, d = qu
        seg.apply(l, r, c << 30 | d)
    else:
        l, r, x = qu
        res = seg.prod(l, r)
        a, b = res >> 30, res & mask
        print((a * x + b) % MOD)
