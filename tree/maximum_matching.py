from tree.rooted_tree import rooted_tree


def max_matching(adj: list[list[int]]) -> list[int]:
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

        p = par[v]
        if p == -1:
            continue

        if selected[v] == selected[p] == 0:
            selected[v] = selected[p] = 1

        deg[p] -= 1
        if deg[p] == 0:
            stack.append(p)

    return selected
