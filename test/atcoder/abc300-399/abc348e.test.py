# verification-helper: PROBLEM https://atcoder.jp/contests/abc348/tasks/abc348_e

from tree.centroids import centroids

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
C = [int(x) for x in input().split()]

center = centroids(g, C)

ans = 0
stack = [(center[0], -1, 1)]
while stack:
    v, p, d = stack.pop()
    for u in g[v]:
        if u != p:
            ans += C[u] * d
            stack.append((u, v, d + 1))
print(ans)
