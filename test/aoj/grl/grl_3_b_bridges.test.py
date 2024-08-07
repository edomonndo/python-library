# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B

from graph.low_link import LowLink

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

L = LowLink(g)
bridges = L.get_bridge()
for u, v in sorted(bridges):
    print(u, v)
