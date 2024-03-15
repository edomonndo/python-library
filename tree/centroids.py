def centroids(adj: list[list[int]], root: int = 0) -> list[int]:
    n = len(adj)
    res = []
    size = [0] * n
    stack = [(~root, -1), (root, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            size[v] = 1
            is_centroid = True
            for u in adj[v]:
                if u == p:
                    continue
                stack.append((~u, v))
                stack.append((u, v))
        else:
            v = ~v
            for u in adj[v]:
                if u == p:
                    continue
                size[v] += size[u]
                if size[v] > n // 2:
                    is_centroid = False
            if n - size[v] > n // 2:
                is_centroid = False
            if is_centroid:
                res.append(v)
    return res
