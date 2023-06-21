# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter
from typing import Tuple, List


def diameter(N: int, G: List[List[int]]) -> Tuple[int, List[int]]:
    def dfs(start: int):
        dist = [-1 for _ in range(N)]
        dist[start] = 0
        stack = [start]
        while stack:
            v = stack.pop()
            for u, d in G[v]:
                if dist[u] != -1:
                    continue
                dist[u] = dist[v] + d
                stack.append(u)
        max_v = -1
        max_d = -1
        for v, d in enumerate(dist):
            if d > max_d:
                max_d = d
                max_v = v
        return max_v, dist

    s, _ = dfs(0)
    v, dist = dfs(s)
    diam = dist[v]
    path = [v]
    while v != s:
        for u, d in G[v]:
            if dist[u] + d == dist[v]:
                path.append(u)
                v = u
                break
    return diam, path


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

diam, path = diameter(N, G)
print(diam, len(path))
print(*path)
