# verification-helper: PROBLEM https://judge.yosupo.jp/problem/global_minimum_cut_of_dynamic_star_augmented_graph


import sys

input = sys.stdin.readline

from graph.extreme_vertex_set import extreme_vertex_set
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.segtree.lazy_segment_tree import LazySegtree


def mapping(x, f):
    return x + f


def composition(f, g):
    return f + g


n, m, q = map(int, input().split())
A = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(m)]

new_edges = extreme_vertex_set(n, edges)
sz = 2 * n - 1
hld = HeavyLightDecomposition(sz, new_edges, sz - 1, True)
vs = [0] * sz
for i in range(sz):
    for v, w in hld.adj[i]:
        vs[hld.into[v]] = w
inf = float("inf")
seg = LazySegtree(vs, min, inf, mapping, composition, 0)


def update(v: int, cost: int):
    # assert 0 <= v < n
    hld.path_query(v, sz - 1, (lambda l, r: seg.apply(l, r, cost - cur[v])))
    cur[v] = cost


cur = [0] * n
for i in range(n):
    update(i, A[i])

for _ in range(q):
    x, y = map(int, input().split())
    update(x, y)
    print(seg.all_prod())
