# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A

from graph.maxflow import MaxFlow

n, m = map(int, input().split())
g = MaxFlow(n)
for _ in range(m):
    u, v, c = map(int, input().split())
    g.add_edge(u, v, c)

ans = g.flow(0, n - 1)
print(ans)
