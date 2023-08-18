# verification-helper: IGNORE

from graph.topological_sort import topological_sort

N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    deg[v] += 1

ans = topological_sort(N, G, deg)
print(*ans, sep="\n")
