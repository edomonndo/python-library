def scc(n: int, edges: list[tuple[int, int]]) -> tuple[list[list[int]], list[int]]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    low = [0] * n
    comp_num = [0] * n
    par = [-1] * n
    ord = [-1] * n
    st1, st2 = [], []
    groups = []
    idx = 0
    for i in range(n):
        if ord[i] != -1:
            continue
        st1 += [i, i]
        while st1:
            v = st1.pop()
            if ord[v] == -1:
                low[v] = ord[v] = idx
                idx += 1
                st2.append(v)
                for u in adj[v]:
                    if ord[u] == -1:
                        st1 += [u, u]
                        par[u] = v
                        continue
                    low[v] = min(low[v], ord[u])
            else:
                if low[v] == ord[v]:
                    group = []
                    u = None
                    while u != v:
                        u = st2.pop()
                        ord[u] = n
                        comp_num[u] = len(groups)
                        group.append(u)
                    groups.append(group)
                p = par[v]
                if p != -1:
                    low[p] = min(low[p], low[v])
    return groups, comp_num
