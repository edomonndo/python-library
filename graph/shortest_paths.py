from heapq import *
from data_structure.basic.leftist_heap import LefitistHeap
from graph.dijkstra import dijkstra


def shortest_paths(n: int, edges: list[tuple[int, int, int]], s: int, t: int, k: int):
    adj = [[] for _ in range(n)]
    adj_rev = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj_rev[v].append((w, u))
    inf = float("inf")
    dist, prev = dijkstra(adj_rev, t)
    if dist[s] == inf:
        return []

    g = [[] for _ in range(n)]
    for u in range(n):
        if prev[u] != -1:
            g[prev[u]].append(u)

    h = [None] * n
    q = [t]
    for u in q:
        seen = False
        for w, v in adj[u]:
            if dist[v] == inf:
                continue
            c = w + dist[v] - dist[u]
            if not seen and v == prev[u] and c == 0:
                seen = True
                continue
            h[u] = LefitistHeap.insert(h[u], c, v)
        for v in g[u]:
            h[v] = h[u]
            q.append(v)

    ans = [dist[s]]
    if not h[s]:
        return ans

    q = [(dist[s] + h[s].key, h[s])]
    while q and len(ans) < k:
        cd, ch = heappop(q)
        ans.append(cd)
        if h[ch.value]:
            heappush(q, (cd + h[ch.value].key, h[ch.value]))
        if ch.left:
            heappush(q, (cd + ch.left.key - ch.key, ch.left))
        if ch.right:
            heappush(q, (cd + ch.right.key - ch.key, ch.right))
    return ans
