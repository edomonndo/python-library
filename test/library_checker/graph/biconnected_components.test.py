# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components

from graph.low_link import LowLink

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
groups = LowLink.biconnected_components_verticle(g)
print(len(groups))
for group in groups:
    print(len(group), *group)
