# verification-helper: PROBLEM https://judge.yosupo.jp/problem/connected_components_of_complement_graph

from graph.connected_components_complement import get_ccc

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

cc = get_ccc(g)
print(len(cc))
for group in cc:
    print(len(group), *cc)
