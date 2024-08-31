# verification-helper: PROBLEM https://yukicoder.me/problems/no/399


from graph.tree.hld_lazysegtree import HldLazySegTree


n = int(input())
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

op = lambda x, y: (x[0] + y[0], x[1] + y[1])
mapping = lambda f, x: (x[0] + f * x[1], x[1])
composition = lambda f, g: f + g
ID = 0
seg = HldLazySegTree(op, (0, 1), mapping, composition, 0, [(0, 1)] * n, n, edges, 0)

q = int(input())
ans = 0
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    tmp1 = seg.path_prod(u, v, False)[0]
    seg.path_apply(u, v, 1, False)
    tmp2 = seg.path_prod(u, v, False)[0]
    ans += seg.path_prod(u, v, False)[0]

print(ans)
