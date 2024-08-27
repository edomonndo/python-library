# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A

from graph.maxflow import maxflow

x, y, m = map(int, input().split())
n = x + y
g = MaxFlow(n + 2)
for _ in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v + x, 1)
for i in range(n):
    if i < x:
        g.add_edge(n, i, 1)
    else:
        g.add_edge(i, n + 1, 1)

f = g.flow(n, n + 1)
print(f)
