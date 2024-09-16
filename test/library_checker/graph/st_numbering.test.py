# verification-helper: PROBLEM https://judge.yosupo.jp/problem/st_numbering

from typing import Optional
import sys

sys.setrecursionlimit(1_000_000)


class STNumbering:
    def __init__(self, n: int):
        self.n = n
        self.edges = []

    def add_edge(self, u: int, v: int) -> None:
        self.edges.append((u, v))

    def solve(self, s: int, t: int) -> Optional[list[int]]:
        n, edges = self.n, self.edges
        if n == 1:
            return [0]
        if s == t:
            return None
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        par = [-1] * n
        pre = [-1] * n
        low = [-1] * n
        pre[s] = 0
        vs = [s]

        st = [(~t, -1), (t, -1)]
        while st:
            v, p = st.pop()
            if v >= 0:
                pre[v] = len(vs)
                vs.append(v)
                low[v] = v
                for u in adj[v]:
                    if u == v:
                        continue
                    if pre[u] == -1:
                        par[u] = v
                        st.append((~u, v))
                        st.append((u, v))
                    elif pre[u] < pre[low[v]]:
                        low[v] = u
                continue
            v = ~v
            if pre[low[v]] < pre[low[p]]:
                low[p] = low[v]

        def dfs(v: int) -> None:
            pre[v] = len(vs)
            vs.append(v)
            low[v] = v
            for u in adj[v]:
                if u == v:
                    continue
                if pre[u] == -1:
                    dfs(u)
                    par[u] = v
                    if pre[low[u]] < pre[low[v]]:
                        low[v] = low[u]
                elif pre[u] < pre[low[v]]:
                    low[v] = u
            return

        # dfs(t)
        if len(vs) < n:
            return None

        nxt = [-1] * n
        prev = [0] * n
        nxt[s], prev[t] = t, s
        sgn = [0] * n
        sgn[s] = -1
        for v in vs[2:]:
            p = par[v]
            if sgn[low[v]] == -1:
                q = prev[p]
                if q == -1:
                    return None
                nxt[q], nxt[v] = v, p
                prev[v], prev[p] = q, v
                sgn[p] = 1
            else:
                q = nxt[p]
                if q == -1:
                    return None
                nxt[p], nxt[v] = v, q
                prev[v], prev[q] = p, v
                sgn[p] = -1

        path = [s]
        while path[-1] != t:
            path.append(nxt[path[-1]])
        if len(path) < n:
            return None

        rank = [-1] * n
        for i, v in enumerate(path):
            rank[v] = i

        for i, v in enumerate(path):
            l, r = 0, 0
            for u in adj[v]:
                if rank[u] < rank[v]:
                    l = 1
                if rank[v] < rank[u]:
                    r = 1
            if i > 0 and l == 0:
                return None
            if i < n - 1 and r == 0:
                return None
        return rank

    def build(self, rank: list[int]) -> list[list[int]]:
        assert len(rank) == self.n
        n, edges = self.n, self.edges
        res = [[] for _ in range(n)]
        for u, v in edges:
            if rank[u] < rank[v]:
                res[u].append(v)
            elif rank[v] < rank[u]:
                res[v].append(u)
        return res


T = int(input())
for _ in range(T):
    n, m, s, t = map(int, input().split())
    g = STNumbering(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)
    ans = g.solve(s, t)
    if ans:
        print("Yes")
        print(*ans)
    else:
        print("No")
