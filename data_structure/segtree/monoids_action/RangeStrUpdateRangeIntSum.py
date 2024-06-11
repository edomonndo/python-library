# https://atcoder.jp/contests/abl/tasks/abl_e

MOD = 998244353

power10 = [1] * (200_001)
one = [0] * (200_001)
for i in range(200_000):
    power10[i + 1] = (power10[i] * 10) % MOD
    one[i + 1] = (one[i] * 10 + 1) % MOD


class S:
    def __init__(self, value=0, size=0):
        self.value = value
        self.size = size

    def __str__(self) -> str:
        return f"({self.value},{self.size})"

    __repr__ = __str__


class F:
    def __init__(self, digit=0):
        self.digit = digit


def op(l: S, r: S) -> S:
    value = (l.value * power10[r.size] + r.value) % MOD
    size = l.size + r.size
    return S(value, size)


def mapping(f: F, x: S) -> S:
    if f.digit == 0:
        return x
    value = f.digit * one[x.size] % MOD
    return S(value, x.size)


def composition(f: F, g: F) -> F:
    if f.digit == 0:
        return g
    return f


"""
from data_structure.segtree.monoids_action.RangeStrUpdateRangeIntSum import *
from atcoder.lazysegtree import LazySegTree

n, q = map(int, input().split())
seg = LazySegTree(op, S(), mapping, composition, F(), [S(1, 1) for _ in range(n)])

for _ in range(q):
    l, r, d = map(int, input().split())
    seg.apply(l - 1, r, F(d))
    print(seg.all_prod().value)
"""
