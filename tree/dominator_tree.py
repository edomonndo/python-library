def dominator_tree(g: list[list[int]], r: int = 0):
    n = len(g)

    # label nodes with the arrival times of a dfs
    sdom = [-1] * n
    par = [-1] * n
    vs = []
    k = 0

    stack = [(r, -1)]
    while stack:
        v, p = stack.pop()
        if sdom[v] != -1:
            continue
        if p != -1:
            par[v] = p
        sdom[v] = k
        k += 1
        vs.append(v)
        for c in g[v]:
            if sdom[c] == -1:
                stack.append((c, v))

    grev = [[] for _ in range(n)]
    for u in range(n):
        if sdom[u] == -1:
            continue
        for v in g[u]:
            grev[v].append(u)

    # Union find
    uf_par = list(range(n))  # parent
    val = list(range(n))  # min of sdom's v

    def compress(v):
        vs = []
        while v != uf_par[v]:
            vs.append(v)
            v = uf_par[v]
        r = v
        for v in vs[::-1]:
            if sdom[val[v]] > sdom[val[uf_par[v]]]:
                val[v] = val[uf_par[v]]
            uf_par[v] = r
        return val[v]

    # calculate sdom
    us = [0] * n
    bucket = [[] for _ in range(n)]
    for w in vs[1:][::-1]:
        for v in grev[w]:
            sdom[w] = min(sdom[w], sdom[compress(v)])
        bucket[vs[sdom[w]]].append(w)
        p = par[w]
        for v in bucket[p]:
            us[v] = compress(v)
        bucket[p] = []
        uf_par[w] = p

    # calculate idom
    idom = [-1] * n
    idom[r] = sdom[r]
    for w in vs[1:]:
        u = us[w]
        idom[w] = sdom[w] if sdom[w] == sdom[u] else idom[u]
    for v in vs:
        idom[v] = vs[idom[v]]
    return idom
