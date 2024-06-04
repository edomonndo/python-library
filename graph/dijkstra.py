from heapq import *


def dijkstra(graph: list[list[int]], start: int) -> tuple[list[int], list[int]]:
    INF = float("inf")
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    prev = [-1] * n

    que = [(0, start)]  # 距離,頂点
    while que:
        c, u = heappop(que)
        if c > dist[u]:
            continue
        for nc, v in graph[u]:
            cost = dist[u] + nc
            if cost < dist[v]:
                dist[v] = cost
                prev[v] = u
                heappush(que, (cost, v))

    return dist, prev


def get_path(prev: list[int], start: int, goal: int) -> list[int]:
    path = [goal]
    while path[-1] != start:
        path.append(prev[path[-1]])
    return path[::-1]
