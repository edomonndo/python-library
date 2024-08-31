# verification-helper: PROBLEM https://atcoder.jp/contests/past202010-open/tasks/past202010_m

from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.segtree.lazy_segment_tree import LazySegtree


n, q = map(int, input().split())
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

hld = HeavyLightDecomposition(n, edges)

inf = float("inf")
mapping = lambda f, x: x if f == ID else f
composition = lambda f, g: g if f == ID else f
ID = inf
seg = LazySegtree([0] * n, lambda x, y: 0, 0, mapping, composition, ID)

for _ in range(q):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    hld.path_query(u, v, (lambda l, r: seg.apply(l, r, c)), True)

ans = None


def f(l, r):
    global ans
    ans = seg.prod(l, r)


for u, v in edges:
    hld.path_query(u, v, f, True)
    print(ans)
