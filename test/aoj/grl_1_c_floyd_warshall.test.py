# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C

from graph.floyd_warshall import floyd_warshall

INF = float("inf")
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

dist = floyd_warshall(N, edges, True)

for i in range(N):
    if dist[i][i] < 0:
        print("NEGATIVE CYCLE")
        exit()

for u in range(N):
    ans = []
    for v in range(N):
        ans.append(dist[u][v] if dist[u][v] != INF else "INF")
    print(*ans)
