# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A

from graph.maxflow import mf_graph

X, Y, M = map(int, input().split())
N = X + Y
G = mf_graph(N + 2)
for _ in range(M):
    x, y = map(int, input().split())
    G.add_edge(x, y + X, 1)
for i in range(N):
    if i < X:
        G.add_edge(N, i, 1)
    else:
        G.add_edge(i, N + 1, 1)

f = G.flow(N, N + 1)
print(f)
