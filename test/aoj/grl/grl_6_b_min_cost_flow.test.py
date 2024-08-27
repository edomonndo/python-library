# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B

from graph.mincostflow import MinCostFlow

n, m, limit = map(int, input().split())
g = MinCostFlow(n)
for _ in range(m):
    u, v, c, d = map(int, input().split())
    g.add_edge(u, v, c, d)

f, c = g.flow(0, n - 1, limit)
print(c if f == limit else -1)
