# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_sequence_range_affine_range_sum
from typing import TypeVar
from data_structure.binary_search_tree.implicit_treap import ImplicitTreap

S = TypeVar("S")
F = TypeVar("F")

MOD = 998244353

msk = (1 << 32) - 1


def op(x: S, y: S) -> S:
    x1, x2 = x >> 32, x & msk
    y1, y2 = y >> 32, y & msk
    return (((x1 + y1) % MOD) << 32) + ((x2 + y2) % MOD)


def mapping(f: F, x: S) -> S:
    f1, f2 = f >> 32, f & msk
    x1, x2 = x >> 32, x & msk
    return (((f1 * x1 % MOD + f2 * x2 % MOD) % MOD) << 32) + x2


def composition(f: F, g: F) -> F:
    f1, f2 = f >> 32, f & msk
    g1, g2 = g >> 32, g & msk
    return ((f1 * g1 % MOD) << 32) + ((f1 * g2 % MOD + f2) % MOD)


n, q = map(int, input().split())
A = [(int(a) << 32) + 1 for a in input().split()]

T = ImplicitTreap(op, 0, mapping, composition, 1 << 32, A)

ans = []
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        i, x = qu
        if i < T.size():
            T.insert(i, (x << 32) + 1)
        else:
            T.insert(T.size(), (x << 32) + 1)
    elif t == 1:
        i = qu[0]
        T.erase(i)
    elif t == 2:
        l, r = qu
        T.reverse(l, r)
    elif t == 3:
        l, r, b, c = qu
        T.apply(l, r, (b << 32) + c)
    else:
        l, r = qu
        ans.append(T.prod(l, r) >> 32)
print(*ans, sep="\n")
