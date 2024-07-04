# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum

from atcoder.fenwicktree import FenwickTree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition


def f(x, y):
    global ans
    ans += bit.sum(x, y)


n, q = map(int, input().split())
A = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
H = HeavyLightDecomposition(n, edges, 0)
P = [0] * n
for i, a in enumerate(A):
    P[H.into[i]] = a
bit = FenwickTree(n)
for i, p in enumerate(P):
    bit.add(i, p)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 0:
        p = H.into[a]
        bit.add(p, b)
    else:
        ans = 0
        H.path_query(a, b, f)
        print(ans)
