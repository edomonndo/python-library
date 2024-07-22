# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components

from graph.biconnected_components import BiconnectedComponents

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
BC = BiconnectedComponents(n, edges)
groups = BC.biconnected_components_verticle()
print(len(groups))
for group in groups:
    print(len(group), *group)
