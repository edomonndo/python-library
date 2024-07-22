# verification-helper: PROBLEM https://judge.yosupo.jp/problem/three_edge_connected_components

from graph.three_edge_connected_components import three_edge_connected_components


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

groups = three_edge_connected_components(g)
print(len(groups))
for group in groups:
    print(len(group), *group)
