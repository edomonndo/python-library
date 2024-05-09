def max_matching(adj: list[list[int]], r: int = 0) -> list[int]:
    n = len(adj)

    selected = [0] * n
    stack = [(r, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            for u in adj[v]:
                if u != p:
                    stack += [(~u, v), (u, v)]
            continue
        if p == -1:
            continue
        v = ~v
        if selected[v] == selected[p] == 0:
            selected[v] = selected[p] = 1

    return selected
