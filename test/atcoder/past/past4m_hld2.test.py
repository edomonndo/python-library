# verification-helper: PROBLEM https://atcoder.jp/contests/past202010-open/tasks/past202010_m

from graph.tree.hld_lazysegtree import HldLazySegTree


n, q = map(int, input().split())
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

inf = float("inf")
mapping = lambda f, x: x if f == ID else f
composition = lambda f, g: g if f == ID else f
ID = inf
seg = HldLazySegTree(min, inf, mapping, composition, ID, [0] * n, n, edges, 0)

for _ in range(q):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    seg.path_apply(u, v, c, True)

for u, v in edges:
    print(seg.path_prod(u, v, True))
