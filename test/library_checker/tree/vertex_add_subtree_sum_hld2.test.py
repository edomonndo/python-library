# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum

from tree.hld_segtree import HldSegtree

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
edges = []
for i, p in enumerate(P, 1):
    edges.append((i, p))

seg = HldSegtree(lambda x, y: x + y, 0, A, n, edges, 0)

for _ in range(q):
    t, *a = map(int, input().split())
    if t == 0:
        v, x = a
        seg.set(v, x + seg.get(v))
    else:
        print(seg.subtree_prod(a[0]))
