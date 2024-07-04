# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree

from graph.tree.heavy_light_decomposition import HeavyLightDecomposition

n, q = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n)]

T = HeavyLightDecomposition(n, edges)
for _ in range(q):
    s, t, k = map(int, input().split())
    print(T.jump(s, t, k))
