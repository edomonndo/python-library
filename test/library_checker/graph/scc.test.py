# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc

from graph.scc import scc

N, M = map(int, input().split())
edges = [None] * M
for i in range(M):
    edges[i] = tuple(map(int, input().split()))

groups = scc(N, edges)
print(len(groups))
for group in groups:
    print(len(group), *group)
