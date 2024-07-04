def min_edge_cover(adj: list[list[int]], r: int = 0) -> tuple[int, list[int]]:
    n = len(adj)

    selected = [0] * n
    cnt_selected_edge = 0
    stack = [(~r, -1), (r, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0 and selected[v] == 0:
            for u in adj[v]:
                if u != p:
                    stack += [(~u, v), (u, v)]
            continue
        v = ~v
        if selected[v] == 0:
            selected[v] = selected[p] = 1
            cnt_selected_edge += 1

    return cnt_selected_edge, selected
