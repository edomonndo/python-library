# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B

from graph.low_link import LowLink

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

LL = LowLink(g)
bridges = LL.get_bridge()
for u, v in bridges:
    print(u, v)
