from typing import Callable, TypeVar

T = TypeVar("T")


def enumerate_triangles(
    n: int,
    edges: tuple[int, int],
    calc: Callable[[T, T], T],
    merge: Callable[[T, T], T],
    e: T = 0,
) -> T:
    adj = [[] for _ in range(n)]
    deg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    tmp = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            if deg[u] > deg[v] or (deg[u] == deg[v] and u > v):
                tmp[u].append(v)

    used = [0] * n
    res = e
    for u in range(n):
        for v in tmp[u]:
            used[v] = 1
        for v in tmp[u]:
            for w in tmp[v]:
                if used[w]:
                    res = merge(res, calc(u, v, w))
        for v in tmp[u]:
            used[v] = 0
    return res
