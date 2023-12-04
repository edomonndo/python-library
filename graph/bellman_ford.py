def bellmanFord(G: list[list[int]], start: int = 0):
    INF = float("inf")
    n = len(G)
    dist = [INF] * n
    pre = [-1] * n
    dist[start] = 0
    loop = 0
    for i in range(n):
        loop += 1
        updated = False
        for u in range(n):
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
        if i == n - 1:
            return -1, -1
    return dist, pre
