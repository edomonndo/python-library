# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components

from graph.low_link import LowLink

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

LL = LowLink(g)
components, _ = LL.two_edge_connected_components()
groups = dict()
for i, ci in enumerate(components):
    if ci in groups:
        groups[ci].append(i)
    else:
        groups[ci] = [i]

print(len(groups))
ans = []
for group in groups.values():
    tmp = [len(group)]
    tmp += group
    ans.append(" ".join(map(str, tmp)))
print(*ans, sep="\n")
