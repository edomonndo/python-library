from collections import deque


def topological_sort(G, deg):
    n = len(G)
    cands = [v for v in range(n) if deg[v] == 0]
    ans = []
    que = deque(cands)
    while que:
        v = que.popleft()
        if v in cands:
            ans.append(v)
        for u in G[v]:
            deg[u] -= 1
            if deg[u] == 0:
                que.append(u)
                ans.append(u)
    if len(ans) == n:
        return ans
    return -1
