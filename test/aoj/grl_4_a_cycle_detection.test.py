# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_A

from graph.topological_sort import topological_sort

N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    deg[v] += 1

ans = topological_sort(G, deg)
print(1 if ans == -1 else 0)
