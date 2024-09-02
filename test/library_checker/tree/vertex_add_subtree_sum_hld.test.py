# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum

from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from graph.tree.heavy_light_decomposition import HLD

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for i, p in enumerate(P, 1):
    g[p].append(i)
hld = HLD(n, g, is_undirect=False)
L = hld.build_list(A)
bit = FenwickTree(n)
for i, p in enumerate(L):
    bit.add(i, p)

for _ in range(q):
    t, *a = map(int, input().split())
    if t == 0:
        v, x = a
        bit.add(hld.index(v), x)
    else:
        l, r = hld.subtree_query(a[0])
        print(bit.sum(l, r))
