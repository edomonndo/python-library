# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum


from graph.tree.template import Tree
from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
g = Tree.from_input(n, 0)
hld = HeavyLightDecomposition(n, g)
P = hld.build_list(A)
bit = FenwickTree(n)
for i, p in enumerate(P):
    bit.add(i, p)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 0:
        bit.add(hld.index(p), b)
    else:
        ans = 0
        for l, r in hld.path_query(a, b, False):
            ans += bit.sum(l, r)
        print(ans)
