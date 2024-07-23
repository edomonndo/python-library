def scc(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    start = [0] * (n + 1)
    m = len(edges)
    elist = [0] * m
    for e in edges:
        start[e[0] + 1] += 1
    for i in range(1, n + 1):
        start[i] += start[i - 1]
    counter = start[:]
    for e in edges:
        elist[counter[e[0]]] = e[1]
        counter[e[0]] += 1
    visited = []
    low = [0] * n
    ord = [-1] * n
    ids = [0] * n
    NG = [0, 0]

    def dfs(v: int):
        stack = [(v, -1, 0), (v, -1, 1)]
        while stack:
            v, bef, t = stack.pop()
            if t:
                if bef != -1 and ord[v] != -1:
                    low[bef] = min(low[bef], ord[v])
                    stack.pop()
                    continue
                low[v] = NG[0]
                ord[v] = NG[0]
                NG[0] += 1
                visited.append(v)
                for i in range(start[v], start[v + 1]):
                    to = elist[i]
                    if ord[to] == -1:
                        stack.append((to, v, 0))
                        stack.append((to, v, 1))
                    else:
                        low[v] = min(low[v], ord[to])
            else:
                if low[v] == ord[v]:
                    while True:
                        u = visited.pop()
                        ord[u] = n
                        ids[u] = NG[1]
                        if u == v:
                            break
                    NG[1] += 1
                low[bef] = min(low[bef], low[v])

    for i in range(n):
        if ord[i] == -1:
            dfs(i)
    for i in range(n):
        ids[i] = NG[1] - 1 - ids[i]
    group_num = NG[1]
    counts = [0] * group_num
    for x in ids:
        counts[x] += 1
    groups = [[] for i in range(group_num)]
    for i in range(n):
        groups[ids[i]].append(i)
    return groups
