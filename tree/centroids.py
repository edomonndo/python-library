def centroids(
    adj: list[list[int]], vcost: list[int] = None, root: int = 0
) -> list[int]:
    n = len(adj)
    if vcost is None:
        vcost = [1] * n

    size = vcost[:]
    stack = [(root, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            for u in adj[v]:
                if u != p:
                    stack += [(~u, v), (u, v)]
        elif p != -1:
            size[p] += size[~v]

    half = size[root] // 2
    stack = [(root, -1)]
    res = []
    while stack:
        v, p = stack.pop()
        if v >= 0:
            for u in adj[v]:
                if u != p:
                    stack += [(~u, v), (u, v)]
        else:
            v = ~v
            if any(u != p and size[u] > half for u in adj[v]):
                continue
            if size[root] - size[v] > half:
                continue
            res.append(v)
    return res
