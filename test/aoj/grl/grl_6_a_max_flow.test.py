# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A

from graph.maxflow import mf_graph

N, M = map(int, input().split())
G = mf_graph(N)
for _ in range(M):
    u, v, c = map(int, input().split())
    G.add_edge(u, v, c)

ans = G.flow(0, N - 1)
print(ans)
