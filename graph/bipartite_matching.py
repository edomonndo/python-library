from random import shuffle


def bipartite_matching(
    n: int, m: int, edges: list[tuple[int, int]]
) -> list[tuple[int, int]]:

    shuffle(edges)

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    prev = [-1] * n
    root = [-1] * n
    p = [-1] * n
    q = [-1] * m
    updated = True
    while updated:
        updated = False
        s = []
        for v in range(n):
            if p[v] == -1:
                root[v] = v
                s.append(v)
        i = 0
        while i < len(s):
            v = s[i]
            i += 1
            if p[root[v]] != -1:
                continue
            for u in adj[v]:
                if q[u] == -1:
                    while u != -1:
                        q[u] = v
                        p[v], u = u, p[v]
                        v = prev[v]
                    updated = True
                    break
                u = q[u]
                if prev[u] != -1:
                    continue
                prev[u] = v
                root[u] = root[v]
                s.append(u)
        if updated:
            for v in range(n):
                prev[v] = -1
                root[v] = -1
    return p, q
