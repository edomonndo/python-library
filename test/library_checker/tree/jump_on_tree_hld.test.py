# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree

from graph.tree.template import Tree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition

n, q = map(int, input().split())
g = Tree.from_input(n, 0)

T = HeavyLightDecomposition(n, g)
for _ in range(q):
    s, t, k = map(int, input().split())
    print(T.jump(s, t, k))
