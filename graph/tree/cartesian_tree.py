def cartesian_tree(LIST: list) -> list:
    n = len(LIST)
    parent = [-1] * n
    stack = []
    for i in range(n):
        prv_i = -1
        while stack and LIST[i] < LIST[stack[-1]]:
            prv_i = stack.pop()
        if prv_i != -1:
            parent[prv_i] = i
        if stack:
            parent[i] = stack[-1]
        stack.append(i)
    return parent
