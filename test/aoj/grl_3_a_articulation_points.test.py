# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A

from graph.low_link import low_link

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans, _ = low_link(N, G)
ans.sort()
if ans:
    print(*ans, sep="\n")
