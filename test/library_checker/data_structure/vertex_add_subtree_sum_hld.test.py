# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum

from atcoder.fenwicktree import FenwickTree
from tree.heavy_light_decomposition import HeavyLightDecomposition


def f(x, y):
    global ans
    ans += bit.sum(x, y)


n, q = map(int, input().split())
A = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
edges = []
for i, p in enumerate(P, 1):
    edges.append((i, p))
H = HeavyLightDecomposition(n, edges, 0)
L = [0] * n
for i, a in enumerate(A):
    L[H.into[i]] = a
bit = FenwickTree(n)
for i, p in enumerate(L):
    bit.add(i, p)

for _ in range(q):
    t, *a = map(int, input().split())
    if t == 0:
        v, x = a
        p = H.into[v]
        bit.add(p, x)
    else:
        ans = 0
        H.subtree_query(a[0], f)
        print(ans)
