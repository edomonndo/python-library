from collections import deque


def bfs(G: list[list[int]], s: int, t: int = None):
    n = len(G)
    dist = [-1] * n
    dist[s] = 0

    que = deque([s])
    while que:
        v = que.popleft()
        if t == v:
            return dist[v]
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    return dist
