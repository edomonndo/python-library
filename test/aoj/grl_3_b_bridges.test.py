# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B

from graph.low_link import low_link

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

_, ans = low_link(G)
ans.sort()
for u, v in ans:
    print(u, v)
