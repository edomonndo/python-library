# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C

from graph.scc import scc

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

groups = scc(N, M, edges)
group_id = [0] * N
for i, group in enumerate(groups):
    for v in group:
        group_id[v] = i

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    print(1 if group_id[s] == group_id[t] else 0)
