# verification-helper: PROBLEM https://judge.yosupo.jp/problem/global_minimum_cut_of_dynamic_star_augmented_graph


import sys

input = sys.stdin.readline

from graph.extreme_vertex_set import extreme_vertex_set
from graph.tree.hld_lazysegtree import HldLazySegTree


def mapping(x, f):
    return x + f


def composition(f, g):
    return f + g


n, m, q = map(int, input().split())
A = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(m)]

new_edges = extreme_vertex_set(n, edges)
sz = 2 * n - 1
inf = float("inf")
seg = HldLazySegTree(
    min, inf, mapping, composition, 0, [0] * sz, sz, new_edges, sz - 1, True
)
for u, v, w in new_edges:
    seg.path_apply(u, v, w, True)

cur = [0] * n
for i in range(n):
    seg.path_apply(i, sz - 1, A[i] - cur[i], False)
    cur[i] = A[i]

for _ in range(q):
    x, y = map(int, input().split())
    seg.path_apply(x, sz - 1, y - cur[x], False)
    cur[x] = y
    print(seg.all_prod())
