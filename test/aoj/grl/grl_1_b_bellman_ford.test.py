# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B

from graph.bellman_ford import BellmanFord

inf = float("inf")
n, m, r = map(int, input().split())
g = BellmanFord(n)
for _ in range(m):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

dist = g.solve_sssp(r)
if dist == -1:
    print("NEGATIVE CYCLE")
    exit()

for d in dist:
    if d == inf:
        print("INF")
    else:
        print(d)
