# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B

from graph.bellman_ford import bellmanFord

INF = float("inf")
N, M, r = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((w, v))

dist, _ = bellmanFord(N, G, r)
if dist == -1:
    print("NEGATIVE CYCLE")
    exit()

for d in dist:
    if d == INF:
        print("INF")
    else:
        print(d)
