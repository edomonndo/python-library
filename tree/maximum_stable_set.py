from tree.rooted_tree import rooted_tree


def max_stable_set(adj: list[list[int]]) -> list[int]:
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
        all_children_not_selected = all(selected[u] == 0 for u in children[v])
        if all_children_not_selected:
            selected[v] = 1

        nv = par[v]
        deg[nv] -= 1
        if deg[nv] == 0:
            stack.append(nv)

    return selected
