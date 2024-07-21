# verification-helper: PROBLEM https://judge.yosupo.jp/problem/three_edge_connected_components

from graph.low_link import LowLink


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

groups = LowLink.three_edge_connected_components(g)
print(len(groups))
for group in groups:
    print(len(group), *group)
