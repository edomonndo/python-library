# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A

from graph.low_link import LowLink

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

LL = LowLink(g)
articulation = LL.get_articulation()
ans = [i for i, v in articulation if v]
if ans:
    print(*ans, sep="\n")
