# verification-helper: PROBLEM https://yukicoder.me/problems/no/399


from graph.tree.template import Tree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.segtree.lazy_segment_tree import LazySegtree

n = int(input())
g = Tree.from_input(n, 1)
hld = HeavyLightDecomposition(n, g, 0, 0)

op = lambda x, y: (x[0] + y[0], x[1] + y[1])
mapping = lambda f, x: (x[0] + f * x[1], x[1])
composition = lambda f, g: f + g
ID = 0
seg = LazySegtree([(0, 1)] * n, op, (0, 1), mapping, composition, 0)

q = int(input())
ans = 0
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    for l, r in hld.path_query(u, v, False):
        seg.apply(l, r, 1)
    for l, r in hld.path_query(u, v, False):
        ans += seg.prod(l, r, False)[0]

print(ans)
