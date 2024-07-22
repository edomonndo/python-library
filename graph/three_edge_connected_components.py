import sys

sys.setrecursionlimit(2_000_000)


def three_edge_connected_components(adj: list[list[int]]) -> list[list[int]]:

    def _enumerate(v: int) -> list[int]:
        res = []
        u = v
        while True:
            res.append(u)
            seen[u] = 1
            u = nxt[u]
            if u == v:
                break
        return res

    def _absorb(u: int, v: int) -> None:
        deg[u] += deg[v]
        nxt[u], nxt[v] = nxt[v], nxt[u]

    def _dfs(v: int, p: int) -> None:
        nonlocal id_
        seen[v] = 1
        pre[v] = id_
        id_ += 1
        for u in adj[v]:
            if u == v:
                continue
            if u == p:
                p = n
                continue
            if seen[u]:
                if pre[u] < pre[v]:
                    deg[v] += 1
                    low[v] = min(low[v], pre[u])
                else:
                    deg[v] -= 1
                    w = path[v]
                    while w != n and pre[w] <= pre[u] < post[w]:
                        _absorb(v, w)
                        w = path[w]
                    path[v] = w
                continue
            _dfs(u, v)
            if path[u] == n and deg[u] <= 1:
                deg[v] += deg[u]
                low[v] = min(low[v], low[u])
                continue
            if deg[u] == 0:
                u = path[u]
            if low[v] > low[u]:
                low[v] = low[u]
                u, path[v] = path[v], u
            while u != n:
                _absorb(v, u)
                u = path[u]
        post[v] = id_

    n = len(adj)
    seen = [0] * n
    pre = [-1] * n
    post = [0] * n
    path = [n] * n
    low = [n] * n
    deg = [0] * n
    nxt = list(range(n))

    id_ = 0
    for i in range(n):
        if not seen[i]:
            _dfs(i, n)

    res = []
    seen = [0] * n
    for i in range(n):
        if not seen[i]:
            res.append(_enumerate(i))
    return res
