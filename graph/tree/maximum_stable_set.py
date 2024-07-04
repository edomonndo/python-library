def max_stable_set(adj: list[list[int]], r: int = 0) -> list[int]:
    n = len(adj)

    selected = [0] * n
    stack = [(~r, -1), (r, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            for u in adj[v]:
                if u != p:
                    stack += [(~u, v), (u, v)]
            continue
        v = ~v
        all_children_not_selected = all(selected[u] == 0 for u in adj[v] if u != p)
        if all_children_not_selected:
            selected[v] = 1

    return selected
