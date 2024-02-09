# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path

from graph.dijkstra import dijkstra, get_path

INF = float("inf")
N, M, s, t = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((c, v))

dist, prev = dijkstra(G, s)

if dist[t] == INF:
    print(-1)
    exit()

path = get_path(prev, s, t)
print(dist[t], len(path) - 1)
for i in range(len(path) - 1):
    print(path[i], path[i + 1])
