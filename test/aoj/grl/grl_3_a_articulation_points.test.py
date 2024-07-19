# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A

from graph.low_link import LowLink

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

L = LowLink(g)
ans = L.get_articulation()
if ans:
    print(*ans, sep="\n")
