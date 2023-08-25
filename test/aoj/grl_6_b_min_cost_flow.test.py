# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B

from graph.mincostflow import mcf_graph

N, M, F = map(int, input().split())
G = mcf_graph(N)
for _ in range(M):
    u, v, c, d = map(int, input().split())
    G.add_edge(u, v, c, d)

f, c = G.flow(0, N - 1, F)
print(c if f == F else -1)
