from collections import deque


def bfs(N, G, s):
    dist = [-1] * N
    dist[s] = 0

    que = deque([s])
    while que:
        v = que.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    return dist
