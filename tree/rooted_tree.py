def rooted_tree(adj: list[list[int]], r: int = 0) -> tuple[list[list[int]], list[int]]:
    n = len(adj)
    children = [[] for _ in range(n)]
    parent = [-1] * n
    seen = [0] * n
    seen[r] = 1
    stack = [r]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if not seen[u]:
                seen[u] = 1
                children[v].append(u)
                parent[u] = v
                stack.append(u)
    return children, parent
