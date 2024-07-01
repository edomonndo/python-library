# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum

from tree.hld_segtree import HldSegtree


n, q = map(int, input().split())
A = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
seg = HldSegtree(lambda x, y: x + y, 0, A, n, edges, 0)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 0:
        seg.set(a, b)
    else:
        print(seg.path_prod(a, b))
