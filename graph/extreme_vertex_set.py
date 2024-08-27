from heapq import *
from typing import TypeVar

T = TypeVar("T")


def extreme_vertex_set(
    n: int, edges: list[tuple[int, int, T]]
) -> list[tuple[int, int, T]]:
    # for u, v, w in edges:
    #    assert 0 <= u < n
    #    assert 0 <= v < n
    #    assert u != v
    #    assert 0 <= w

    res = []
    uf = list(range(n))
    cur = [0] * (2 * n - 1)
    leaf = [1] * n + [0] * (n - 1)

    pq = []
    for t in range(n - 1):
        g = [[] for _ in range(2 * n - 1)]
        cost = [0] * (2 * n - 1)
        for i in range(len(edges)):
            u, v, w = edges[i]
            u = uf[u]
            v = uf[v]
            if u != v:
                cost[u] += w
                cost[v] += w
                g[u].append((v, w))
                g[v].append((u, w))
        for i in range(2 * n - 1):
            if leaf[i]:
                cur[i] = cost[i]
                heappush(pq, (cost[i], i))
        x = y = -1
        while pq:
            _, v = heappop(pq)
            if cur[v] == -1:
                continue
            cur[v] = -1
            x, y = v, x
            for u, w in g[v]:
                if cur[u] != -1:
                    cur[u] -= w
                    heappush(pq, (cur[u], u))
        z = n + t
        res += [(z, x, cost[x]), (z, y, cost[y])]
        for i in range(n):
            if uf[i] == x or uf[i] == y:
                uf[i] = z
        leaf[x] = leaf[y] = 0
        leaf[z] = 1
    return res
