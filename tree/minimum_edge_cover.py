from tree.rooted_tree import rooted_tree


def min_edge_cover(adj: list[list[int]]) -> tuple[int, list[int]]:
    n = len(adj)
    children, par = rooted_tree(adj, 0)

    deg = [0] * n
    stack = []
    for v in range(n):
        deg[v] = len(children[v])
        if deg[v] == 0:
            stack.append(v)

    selected = [0] * n
    cnt_selected_edge = 0
    while stack:
        v = stack.pop()
        p = par[v]

        if selected[v] == 0:
            selected[v] = selected[p] = 1
            cnt_selected_edge += 1

        deg[p] -= 1
        if deg[p] == 0:
            stack.append(p)

    return cnt_selected_edge, selected
