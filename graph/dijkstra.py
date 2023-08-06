from typing import List, Tuple
from heapq import heappush, heappop


def dijkstra(N: int, graph: List[List[int]], start: int) -> Tuple[List[int], List[int]]:
    INF = 1 << 60
    dist = [INF] * N
    dist[start] = 0
    prev = [-1] * N

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


def get_path(prev: List[int], start: int, goal: int) -> List[int]:
    path = [goal]
    while path[-1] != start:
        path.append(prev[path[-1]])
    return path[::-1]
