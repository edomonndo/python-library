from tree.rooted_tree import rooted_tree


def min_vertex_cover(adj: list[list[int]]) -> list[int]:
    n = len(adj)
    children, par = rooted_tree(adj, 0)

    deg = [0] * n
    stack = []
    for v in range(n):
        deg[v] = len(children[v])
        if deg[v] == 0:
            stack.append(v)

    selected = [0] * n
    while stack:
        v = stack.pop()

        has_not_selected_v = any(selected[u] == 0 for u in children[v])
        if has_not_selected_v:
            selected[v] = 1

        p = par[v]
        deg[p] -= 1
        if deg[p] == 0:
            stack.append(p)

    return selected
