def floyd_warshall(
    N: int, edges: list[tuple[int, int, int]], directed=False
) -> list[list[int]]:
    INF = float("inf")
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        if not directed:
            dist[v][u] = w

    for i in range(N):
        for u in range(N):
            for v in range(N):
                nd = dist[u][i] + dist[i][v]
                if dist[u][v] > nd:
                    dist[u][v] = nd

    return dist
