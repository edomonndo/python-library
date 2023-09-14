def bellmanFord(N: int, G: list[list[int]], start: int = 0):
    INF = float("inf")
    dist = [INF] * N
    pre = [-1] * N
    dist[start] = 0
    loop = 0
    for i in range(N):
        loop += 1
        updated = False
        for u in range(N):
            if dist[u] == INF:
                continue
            for w, v in G[u]:
                nd = dist[u] + w
                if nd < dist[v]:
                    updated = True
                    pre[v] = u
                    dist[v] = nd
        if not updated:
            break
        if i == N - 1:
            return -1, -1
    return dist, pre
