# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/2667

from graph.tree.heavy_light_decomposition import HLD
from data_structure.segtree.lazy_segment_tree import LazySegtree

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
hld = HLD(n, g)


def op(x, y):
    return (x[0] + y[0], x[1] + y[1])


e = (0, 1)
mapping = lambda f, x: (x[0] + f * x[1], x[1])
composition = lambda f, g: f + g
ID = 0
seg = LazySegtree([e] * n, op, e, mapping, composition, ID)

for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        ans = e
        for l, r in hld.path_query(u, v, True):
            ans = op(ans, seg.prod(l, r))
        print(ans[0])
    else:
        l, r = hld.subtree_query(u, True)
        seg.apply(l, r, v)
