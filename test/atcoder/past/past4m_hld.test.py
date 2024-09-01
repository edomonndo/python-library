# verification-helper: PROBLEM https://atcoder.jp/contests/past202010-open/tasks/past202010_m

from graph.tree.template import Tree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.segtree.lazy_segment_tree import LazySegtree


n, q = map(int, input().split())
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
g = [[] for _ in range(n)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)
hld = HeavyLightDecomposition(n, g)

inf = float("inf")
mapping = lambda f, x: x if f == ID else f
composition = lambda f, g: g if f == ID else f
ID = inf
seg = LazySegtree([0] * n, min, inf, mapping, composition, ID)

for _ in range(q):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    for l, r in hld.path_query(u, v, True):
        seg.apply(l, r, c)


for u, v in edges:
    ans = None
    for l, r in hld.path_query(u, v, True):
        ans = seg.prod(l, r)
    print(ans)
