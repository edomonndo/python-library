# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A

from graph.dijkstra import dijkstra

INF = float("inf")
N, M, r = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((w, v))

dist, _ = dijkstra(N, G, r)
for i in range(N):
    print(dist[i] if dist[i] != INF else "INF")
